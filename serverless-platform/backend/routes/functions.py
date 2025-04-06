from fastapi import APIRouter, UploadFile, File, Form
from backend.models.functionModel import FunctionModel
from backend.controllers import functionController
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/")
def create_function_handler(function: FunctionModel):
    return functionController.create_function(function)

@router.get("/")
def list_all():
    return functionController.get_all_functions()

@router.get("/{func_id}")
def get(func_id: str):
    return functionController.get_function_by_id(func_id)

@router.delete("/{func_id}")
def delete(func_id: str):
    return functionController.delete_function(func_id)

@router.post("/upload")
async def upload_function(
    file: UploadFile = File(...),
    runtime: str = Form("python")
):
    return await functionController.upload_function(file, runtime)

@router.post("/{func_id}/execute")
def execute_function(func_id: str):
    return functionController.execute_function(func_id)

