from fastapi import FastAPI,HTTPException

from database.db import Base,engine,Sessionlocal

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Inventory Management System")

