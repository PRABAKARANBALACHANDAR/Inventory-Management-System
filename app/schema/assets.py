from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime,Integer,String
from sqlalchemy.orm import Mapped,mapped_column
from app.database.db import Base

class Asset(Base):
    __tablename__="assets"
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    category:Mapped[Optional[str]]=mapped_column(String(50),nullable=True)
    price:Mapped[int]=mapped_column(Integer,nullable=False)
    quantity:Mapped[int]=mapped_column(Integer,nullable=False)
    provided_at:Mapped[datetime]=mapped_column(DateTime,nullable=False)
    warranty_end:Mapped[Optional[datetime]]=mapped_column(DateTime,nullable=True)
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    updated_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    
