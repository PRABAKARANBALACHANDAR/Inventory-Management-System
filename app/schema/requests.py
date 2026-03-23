from datetime import datetime
from sqlalchemy import DateTime,ForeignKey,Integer,String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.database.db import Base

class Request(Base):
    __tablename__="requests"
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    asset_name:Mapped[str]=mapped_column(String(50),nullable=False)
    req_by:Mapped[int]=mapped_column(ForeignKey("employees.id"),nullable=False)
    req_qty:Mapped[int]=mapped_column(Integer,nullable=False)
    req_date:Mapped[datetime]=mapped_column(DateTime,nullable=False,default=datetime.utcnow)
    status:Mapped[str]=mapped_column(String(20),nullable=False,default="pending")
    employee=relationship("Employee",back_populates="requests")
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    updated_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
