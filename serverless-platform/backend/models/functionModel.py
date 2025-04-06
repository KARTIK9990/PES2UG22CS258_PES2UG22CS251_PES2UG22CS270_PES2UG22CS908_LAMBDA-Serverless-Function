from pydantic import BaseModel
from typing import Optional

class FunctionModel(BaseModel):
    name: str
    language: str  
    code: str
    timeout: Optional[int] = 5  
