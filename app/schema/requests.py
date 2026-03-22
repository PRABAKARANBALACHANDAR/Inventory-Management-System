from sqlalchemy import String,Integer,DateTime,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from database.db import Base

class Request(Base):
    __tablename__="requests"
    id=Mapped[int]=mapped_column(primary_key=True)
    asset_name=Mapped[str]=mapped_column(String(50),nullable=False)
    req_by=Mapped[int]=mapped_column(ForeignKey("employees.id"),nullable=False)
    req_qty=Mapped[int]=mapped_column(Integer,nullable=False)
    req_date=Mapped[DateTime]=mapped_column(DateTime,nullable=False)
    status=Mapped[str]=mapped_column(String(20),nullable=False,default="pending")
    created_at=Mapped[DateTime]=mapped_column(DateTime,nullable=False)
    updated_at=Mapped[DateTime]=mapped_column(DateTime,nullable=False)
    employee=relationship("Employee",back_populates="requests")
    created_at=Mapped[DateTime]=mapped_column(DateTime,default=DateTime.now)
    updated_at=Mapped[DateTime]=mapped_column(DateTime,default=DateTime.now)