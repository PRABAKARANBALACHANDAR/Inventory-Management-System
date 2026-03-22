from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Integer,DateTime
from database.db import Base

class Asset(Base):
    __tablename__="assets"
    id=Mapped[int]=mapped_column(primary_key=True)
    name=Mapped[str]=mapped_column(String(50),nullable=False)
    category=Mapped[str]=mapped_column(String(50),nullable=True)
    quantity=Mapped[int]=mapped_column(Integer,nullable=False)
    provided_at=Mapped[DateTime]=mapped_column(DateTime,nullable=False)
    warranty_end=Mapped[DateTime]=mapped_column(DateTime,nullable=True)
    created_at=Mapped[DateTime]=mapped_column(DateTime,default=DateTime.now)
    updated_at=Mapped[DateTime]=mapped_column(DateTime,default=DateTime.now,onupdate=DateTime.now)
    