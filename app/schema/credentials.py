from datetime import datetime
from sqlalchemy import DateTime,String
from sqlalchemy.orm import Mapped,mapped_column
from app.database.db import Base

class Credentials(Base):
    __tablename__="credentials"
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    username:Mapped[str]=mapped_column(String(20),nullable=False,unique=True,index=True)
    password:Mapped[str]=mapped_column(String(50),nullable=False)
    role:Mapped[str]=mapped_column(String(20),nullable=False,default="admin")
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    updated_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
