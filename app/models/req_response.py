from datetime import datetime
from typing import Optional
from pydantic import BaseModel,ConfigDict

class RequestCreate(BaseModel):
    asset_name:str
    req_by:int
    req_qty:int
    req_date:Optional[datetime]=None
    status:str="pending"

class RequestUpdate(BaseModel):
    asset_name:Optional[str]=None
    req_by:Optional[int]=None
    req_qty:Optional[int]=None
    req_date:Optional[datetime]=None
    status:Optional[str]=None

class RequestRead(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    asset_name:str
    req_by:int
    req_qty:int
    req_date:datetime
    status:str
    created_at:datetime
    updated_at:datetime
