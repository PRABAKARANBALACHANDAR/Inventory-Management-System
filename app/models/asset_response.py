from datetime import datetime
from typing import Optional
from pydantic import BaseModel,ConfigDict

class AssetCreate(BaseModel):
    name:str
    category:Optional[str]=None
    price:int
    quantity:int
    provided_at:datetime
    warranty_end:Optional[datetime]=None

class AssetUpdate(BaseModel):
    name:Optional[str]=None
    category:Optional[str]=None
    price:Optional[int]=None
    quantity:Optional[int]=None
    provided_at:Optional[datetime]=None
    warranty_end:Optional[datetime]=None

class AssetRead(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    name:str
    category:Optional[str]
    price:int
    quantity:int
    provided_at:datetime
    warranty_end:Optional[datetime]
    created_at:datetime
    updated_at:datetime
