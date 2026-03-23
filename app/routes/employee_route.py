from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.auth.login import get_admin_user,get_current_user
from app.database.db import get_db
from app.exceptions.custom_errors import ConflictException,NotFoundException
from app.models.employee_response import EmployeeCreate,EmployeeRead,EmployeeUpdate
from app.schema.employees import Employee
from app.schema.credentials import Credentials
import bcrypt
router=APIRouter(prefix="/employees",tags=["employees"],dependencies=[Depends(get_current_user)])

@router.get("/",response_model=list[EmployeeRead])
def get_employees(db:Session=Depends(get_db)):
    return db.query(Employee).order_by(Employee.id).all()

@router.get("/{employee_id}",response_model=EmployeeRead)
def get_employee(employee_id:int,db:Session=Depends(get_db)):
    employee=db.query(Employee).filter(Employee.id==employee_id).first()
    if not employee:
        raise NotFoundException("Employee not found")
    return employee

@router.post("/",response_model=EmployeeRead,status_code=status.HTTP_201_CREATED,dependencies=[Depends(get_admin_user)])
def create_employee(employee:EmployeeCreate,db:Session=Depends(get_db)):
    existing=db.query(Employee).filter(Employee.name==employee.name,Employee.dept==employee.dept).first()
    if existing:
        raise ConflictException("Employee already exists")
    new_employee=Employee(name=employee.name,dept=employee.dept,is_hr=employee.is_hr,is_manager=employee.is_manager)
    if employee.is_hr:
        role="HR"
    else:
        role="Manager"
    employee.password=b"{employee.password}"
    new_credential=Credentials(username=employee.username,password=bcrypt.hashpw(employee.password),role=role)
    db.add(new_credential,new_employee)
    db.commit()
    db.refresh(new_employee,new_credential)
    return new_employee

@router.put("/{employee_id}",response_model=EmployeeRead,dependencies=[Depends(get_admin_user)])
def update_employee(employee_id:int,employee:EmployeeUpdate,db:Session=Depends(get_db)):
    existing=db.query(Employee).filter(Employee.id==employee_id).first()
    if not existing:
        raise NotFoundException("Employee not found")
    for key,value in employee.model_dump(exclude_unset=True).items():
        setattr(existing,key,value)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete("/{employee_id}",dependencies=[Depends(get_admin_user)])
def delete_employee(employee_id:int,db:Session=Depends(get_db)):
    employee=db.query(Employee).filter(Employee.id==employee_id).first()
    if not employee:
        raise NotFoundException("Employee not found")
    db.delete(employee)
    db.commit()
    return {"message":"Employee deleted successfully"}
