from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional

class EmployeeCreate(BaseModel):
    id=int
    name=str
    dept=str
    is_hr=bool
    is_manager=bool
    created_at=datetime
    updated_at=datetime
    
class EmplopyeeUpdate(BaseModel):
    name=Optional[str]
    dept=Optional[str]
    is_hr=bool
    is_manager=bool
    updated_at=datetime

class EmployeeRead(BaseModel):
    id=int
    name=str
    dept=Optional[str]
    is_hr=bool
    is_manager=bool
    created_at=datetime