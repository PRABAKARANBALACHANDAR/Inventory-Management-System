from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,Integer,DateTime,ForeignKey
from database.db import Base

class Audit(Base):
    __tablename__="audit"
    id=Mapped[int]=mapped_column(Integer,ForeignKey("assets.id"))
    asset_name=Mapped[str]=mapped_column(String(50),ForeignKey("assets.name"),nullable=False)
    category=Mapped[str]=mapped_column(String(50),ForeignKey("assets.category"),nullable=True)
    price=Mapped[int]=mapped_column(Integer,ForeignKey("assets.price"),nullable=False)
    quantity=Mapped[int]=mapped_column(Integer,ForeignKey("assets.quantity"),nullable=False)
    replaced_at=Mapped[int]=mapped_column(DateTime,nullable=False)
    