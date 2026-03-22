from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional

class AssetCreate(BaseModel):
    id=int
    name=str
    category=Optional[str]
    price=int
    quantity=int
    provided_at=datetime
    created_at=datetime
    updated_at=datetime
    
class AssetUpdate(BaseModel):
    name=Optional[str]
    category=Optional[str]
    price=Optional[int]
    quantity=Optional[int]
    updated_at=datetime

class AssetRead(BaseModel):
    id=int
    name=str
    category=Optional[str]
    price=int
    quantity=int
    provided_at=datetime
    created_at=datetime