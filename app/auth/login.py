from fastapi import APIRouter,Response,Depends,HTTPException
from database.db import Sessionlocal,get_db
from dotenv import load_dotenv
from schema import credentials
import os
import jwt
from pydantic import BaseModel
from datetime import datetime,timedelta

env_path=os.path.join(os.path.dirname(__file__),"..",".env")
load_dotenv(env_path)

ADMIN_USERNAME=os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD=os.getenv("ADMIN_PASSWORD")
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
EXP_MINUTES=os.getenv("JWT_EXPIRE_MINUTES")


class Login(BaseModel):
    username=str
    password=str
    
router=APIRouter(prefix="auth",tags=["auth"])

@router.on_event("startup")
def startup():
    try:
        db=Sessionlocal()
        existing=db.query(credentials).filter(credentials.role=="admin").first()
        if not existing:
            admin=credentials(username=ADMIN_USERNAME,password=ADMIN_PASSWORD,role="admin")
            db.add(admin)
            db.commit()
    finally:
        db.close()
            
def login(login: Login,response=Response,db=Depends(get_db)):
    try:
        user=db.query(credentials).filter(credentials.username==login.username,credentials.password==login.password).first()
        if not user:
            raise HTTPException(status_code=401,detail="Invalid username or password")
        payload=user.copy()
        payload["exp"]= datetime.utcnow() + timedelta(minutes=EXP_MINUTES)
        token=jwt.encode(payload,SECRET_KEY,ALGORITHM)
        return 
    except:
        raise HTTPException