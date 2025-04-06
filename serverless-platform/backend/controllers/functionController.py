from backend.models.functionModel import FunctionModel
from fastapi import HTTPException, UploadFile
from backend.config.db import get_db
from bson import ObjectId
import subprocess
import os
from datetime import datetime

def create_function(function: FunctionModel):
    db = get_db()
    data = function.dict()
    result = db.functions.insert_one(data)
    return {"id": str(result.inserted_id)}

def get_all_functions():
    db = get_db()
    return [
        {**func, "_id": str(func["_id"])} 
        for func in db.functions.find()
    ]

def get_function_by_id(func_id: str):
    db = get_db()
    func = db.functions.find_one({"_id": ObjectId(func_id)})
    if not func:
        raise HTTPException(status_code=404, detail="Function not found")
    func["_id"] = str(func["_id"])
    return func

def delete_function(func_id: str):
    db = get_db()
    result = db.functions.delete_one({"_id": ObjectId(func_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Function not found")
    return {"status": "deleted"}

UPLOAD_DIR = "uploaded_functions"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def upload_function(file: UploadFile, runtime: str):
    contents = await file.read()
    filename = f"{datetime.utcnow().timestamp()}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(contents)

    # Save metadata to DB
    db = get_db()
    data = {
        "filename": filename,
        "filepath": filepath,
        "runtime": runtime,
        "code": contents.decode("utf-8"),
        "created_at": datetime.utcnow()
    }
    result = db.functions.insert_one(data)

    return {"id": str(result.inserted_id), "filename": filename}


def execute_function(func_id: str):
    db = get_db()
    func = db.functions.find_one({"_id": ObjectId(func_id)})
    if not func:
        raise HTTPException(status_code=404, detail="Function not found")

    runtime = func.get("runtime")
    filepath = func.get("filepath")

    if not filepath or not os.path.exists(filepath):
        raise HTTPException(status_code=400, detail="Function file missing")

    if runtime == "python":
        result = subprocess.run(["docker", "run", "--rm", "-v", f"{os.path.abspath(filepath)}:/code.py", "python-runner"],
                                capture_output=True, text=True)
    elif runtime == "javascript":
        result = subprocess.run(
            ["docker", "run", "--rm", "-v", f"{os.path.abspath(filepath)}:/code.js", "js-runner"],
            capture_output=True, text=True
    )
    else:
        raise HTTPException(status_code=400, detail="Unsupported runtime")

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "exit_code": result.returncode
    }


