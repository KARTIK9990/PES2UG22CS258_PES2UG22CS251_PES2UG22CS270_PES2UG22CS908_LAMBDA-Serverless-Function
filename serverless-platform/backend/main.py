from fastapi import FastAPI
from backend.routes.functions import router as function_router
from backend.config.db import connect_to_mongo

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    connect_to_mongo()

@app.post("/run/python")
def run_python(code: dict):
    return {"output": "5"}

@app.post("/run/javascript")
def run_js(code: dict):
    return {"output": "15"}

app.include_router(function_router, prefix="/functions")