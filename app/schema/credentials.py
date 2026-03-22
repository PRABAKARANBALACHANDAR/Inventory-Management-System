from sqlalchemy import String,DateTime,Date
from sqlalchemy.orm import Mapped,mapped_column
from database.db import Base

class Credentials(Base):
    __tablename__="credentials"
    username=Mapped[str]=mapped_column(String(20),nullable=False)
    password=Mapped[str]=mapped_column(String(50),nullable=False)
    created_at=Mapped[DateTime]=mapped_column(DateTime,default=DateTime.now)
    updated_at=Mapped[DateTime]=mapped_column(DateTime,default=DateTime.now)