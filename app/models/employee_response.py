from datetime import datetime
from typing import Optional
from pydantic import BaseModel,ConfigDict

class EmployeeCreate(BaseModel):
    name:str
    dept:str
    is_hr:bool=False
    is_manager:bool=False
    username:str
    password:str

class EmployeeUpdate(BaseModel):
    name:Optional[str]=None
    dept:Optional[str]=None
    is_hr:Optional[bool]=None
    is_manager:Optional[bool]=None

class EmployeeRead(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:int
    name:str
    dept:str
    is_hr:bool
    is_manager:bool
    created_at:datetime
    updated_at:datetime
