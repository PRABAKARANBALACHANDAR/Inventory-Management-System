from datetime import datetime
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.auth.login import get_admin_user,get_current_user
from app.database.db import get_db
from app.exceptions.custom_errors import NotFoundException
from app.models.req_response import RequestCreate,RequestRead,RequestUpdate
from app.schema.assets import Asset
from app.schema.employees import Employee
from app.schema.requests import Request

router=APIRouter(prefix="/requests",tags=["requests"],dependencies=[Depends(get_current_user)])

@router.get("/",response_model=list[RequestRead])
def get_requests(db:Session=Depends(get_db)):
    return db.query(Request).order_by(Request.id).all()

@router.get("/{request_id}",response_model=RequestRead)
def get_request(request_id:int,db:Session=Depends(get_db)):
    request_obj=db.query(Request).filter(Request.id==request_id).first()
    if not request_obj:
        raise NotFoundException("Request not found")
    return request_obj

@router.post("/",response_model=RequestRead,status_code=status.HTTP_201_CREATED)
def create_request(request:RequestCreate,db:Session=Depends(get_db)):
    employee=db.query(Employee).filter(Employee.id==request.req_by).first()
    if not employee:
        raise NotFoundException("Employee not found")
    asset=db.query(Asset).filter(Asset.name==request.asset_name).first()
    if not asset:
        raise NotFoundException("Asset not found")
    request_data=request.model_dump()
    if not request_data.get("req_date"):
        request_data["req_date"]=datetime.utcnow()
    new_request=Request(**request_data)
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

@router.put("/{request_id}",response_model=RequestRead,dependencies=[Depends(get_admin_user)])
def update_request(request_id:int,request:RequestUpdate,db:Session=Depends(get_db)):
    request_obj=db.query(Request).filter(Request.id==request_id).first()
    if not request_obj:
        raise NotFoundException("Request not found")
    update_data=request.model_dump(exclude_unset=True)
    if "req_by" in update_data:
        employee=db.query(Employee).filter(Employee.id==update_data["req_by"]).first()
        if not employee:
            raise NotFoundException("Employee not found")
    if "asset_name" in update_data:
        asset=db.query(Asset).filter(Asset.name==update_data["asset_name"]).first()
        if not asset:
            raise NotFoundException("Asset not found")
    for key,value in update_data.items():
        setattr(request_obj,key,value)
    db.commit()
    db.refresh(request_obj)
    return request_obj

@router.delete("/{request_id}",dependencies=[Depends(get_admin_user)])
def delete_request(request_id:int,db:Session=Depends(get_db)):
    request_obj=db.query(Request).filter(Request.id==request_id).first()
    if not request_obj:
        raise NotFoundException("Request not found")
    db.delete(request_obj)
    db.commit()
    return {"message":"Request deleted successfully"}
