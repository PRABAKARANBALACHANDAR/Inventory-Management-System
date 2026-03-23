from fastapi import FastAPI
from app.auth.login import bootstrap_admin
from app.database.db import Base,Sessionlocal,engine
from app.exceptions.custom_errors import register_exception_handlers
from app.routes.asset_route import router as asset_router
from app.routes.employee_route import router as employee_router
from app.routes.login_route import router as login_router
from app.routes.request_route import router as request_router
from app.schema.assets import Asset
from app.schema.credentials import Credentials
from app.schema.employees import Employee
from app.schema.requests import Request

app=FastAPI(title="Inventory Management System")
register_exception_handlers(app)

app.include_router(login_router)
app.include_router(employee_router)
app.include_router(asset_router)
app.include_router(request_router)

Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup():
    db=Sessionlocal()
    try:
        bootstrap_admin(db)
    finally:
        db.close()

