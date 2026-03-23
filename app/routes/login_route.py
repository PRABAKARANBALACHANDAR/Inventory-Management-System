from pydantic import BaseModel
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.auth.login import authenticate_user,create_access_token
from app.database.db import get_db
from app.exceptions.custom_errors import UnauthorizedException

class LoginRequest(BaseModel):
    username:str
    password:str

router=APIRouter(prefix="/auth",tags=["auth"])

@router.post("/login")
def login(login:LoginRequest,db:Session=Depends(get_db)):
    user=authenticate_user(login.username,login.password,db)
    if not user:
        raise UnauthorizedException("Invalid username or password")
    token=create_access_token({"username":user.username,"role":user.role})
    return {"access_token":token,"token_type":"bearer","role":user.role}
