import os
from datetime import datetime,timedelta
import jwt
from dotenv import load_dotenv
from fastapi import Depends,status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.exceptions.custom_errors import UnauthorizedException
from app.schema.credentials import Credentials

env_path=os.path.join(os.path.dirname(__file__),"..","..",".env")
load_dotenv(env_path)

ADMIN_USERNAME=os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD=os.getenv("ADMIN_PASSWORD")
SECRET_KEY=os.getenv("SECRET_KEY","secret")
ALGORITHM=os.getenv("ALGORITHM","HS256")
EXP_MINUTES=int(os.getenv("JWT_EXPIRE_MINUTES","30"))

security=HTTPBearer()

def bootstrap_admin(db:Session):
    admin=db.query(Credentials).filter(Credentials.username==ADMIN_USERNAME).first()
    if admin:
        return admin
    admin=Credentials(username=ADMIN_USERNAME,password=ADMIN_PASSWORD,role="admin")
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def authenticate_user(username:str,password:str,db:Session):
    return db.query(Credentials).filter(Credentials.username==username,Credentials.password==password).first()

def create_access_token(data:dict):
    payload=data.copy()
    payload["exp"]=datetime.utcnow()+timedelta(minutes=EXP_MINUTES)
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def decode_access_token(token:str):
    try:
        return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except Exception as exc:
        raise UnauthorizedException("Invalid or expired token") from exc

def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security),db:Session=Depends(get_db)):
    payload=decode_access_token(credentials.credentials)
    username=payload.get("username")
    if not username:
        raise UnauthorizedException("Invalid token payload")
    user=db.query(Credentials).filter(Credentials.username==username).first()
    if not user:
        raise UnauthorizedException("User not found")
    return user

def get_admin_user(user:Credentials=Depends(get_current_user)):
    if user.role!="admin":
        raise UnauthorizedException("Admin access required",status.HTTP_403_FORBIDDEN)
    return user
