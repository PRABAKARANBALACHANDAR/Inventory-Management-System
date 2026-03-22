from database.db import Base
from sqlalchemy import String,Integer,DateTime
from sqlalchemy.orm import Mapped,mapped_column,relationship

class Employee(Base):
    __tablename__="employees"
    id=Mapped[int]=mapped_column(primary_key=True)
    name=Mapped[str]=mapped_column(String(50),nullable=False)
    dept=Mapped[str]=mapped_column(String(50),nullable=False)
    is_hr=Mapped[bool]=mapped_column(nullable=False,default=False)
    is_manager=Mapped[bool]=mapped_column(nullable=False,default=False)
    requests=relationship("Request",back_populates="employee")
    created_at=Mapped[DateTime]=mapped_column(DateTime,default=DateTime.now)
    updated_at=Mapped[DateTime]=mapped_column(DateTime,default=DateTime.now)