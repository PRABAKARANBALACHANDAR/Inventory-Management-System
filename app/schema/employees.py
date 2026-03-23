from datetime import datetime
from sqlalchemy import DateTime,String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.database.db import Base

class Employee(Base):
    __tablename__="employees"
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    dept:Mapped[str]=mapped_column(String(50),nullable=False)
    is_hr:Mapped[bool]=mapped_column(nullable=False,default=False)
    is_manager:Mapped[bool]=mapped_column(nullable=False,default=False)
    requests=relationship("Request",back_populates="employee",cascade="all,delete-orphan")
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    updated_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
