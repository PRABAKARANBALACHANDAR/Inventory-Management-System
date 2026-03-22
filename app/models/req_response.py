from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional

class RequestCreate(BaseModel):
    id=int
    asset_name=str
    req_by=int
    deq_qty=int
    req_date=datetime
    status=str
    created_at=datetime
    updated_at=datetime
    
class RequestUpdate(BaseModel):
    asset_name=str
    req_by=int
    deq_qty=int
    req_date=datetime
    status=str
    updated_at=datetime

class RequestRead(BaseModel):
    id=int
    asset_name=str
    req_by=int
    deq_qty=int
    req_date=datetime
    status=str
    created_at=datetime
    updated_at=datetime
