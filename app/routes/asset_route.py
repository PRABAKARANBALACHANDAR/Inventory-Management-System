from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.auth.login import get_admin_user,get_current_user
from app.database.db import get_db
from app.exceptions.custom_errors import ConflictException,NotFoundException
from app.models.asset_response import AssetCreate,AssetRead,AssetUpdate
from app.schema.assets import Asset

router=APIRouter(prefix="/assets",tags=["assets"],dependencies=[Depends(get_current_user)])

@router.get("/",response_model=list[AssetRead])
def get_assets(db:Session=Depends(get_db)):
    return db.query(Asset).order_by(Asset.id).all()

@router.get("/{asset_id}",response_model=AssetRead)
def get_asset(asset_id:int,db:Session=Depends(get_db)):
    asset=db.query(Asset).filter(Asset.id==asset_id).first()
    if not asset:
        raise NotFoundException("Asset not found")
    return asset

@router.post("/",response_model=AssetRead,status_code=status.HTTP_201_CREATED,dependencies=[Depends(get_admin_user)])
def create_asset(asset:AssetCreate,db:Session=Depends(get_db)):
    existing=db.query(Asset).filter(Asset.name==asset.name,Asset.category==asset.category).first()
    if existing:
        raise ConflictException("Asset already exists")
    new_asset=Asset(**asset.model_dump())
    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)
    return new_asset

@router.put("/{asset_id}",response_model=AssetRead,dependencies=[Depends(get_admin_user)])
def update_asset(asset_id:int,asset:AssetUpdate,db:Session=Depends(get_db)):
    existing=db.query(Asset).filter(Asset.id==asset_id).first()
    if not existing:
        raise NotFoundException("Asset not found")
    for key,value in asset.model_dump(exclude_unset=True).items():
        setattr(existing,key,value)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete("/{asset_id}",dependencies=[Depends(get_admin_user)])
def delete_asset(asset_id:int,db:Session=Depends(get_db)):
    asset=db.query(Asset).filter(Asset.id==asset_id).first()
    if not asset:
        raise NotFoundException("Asset not found")
    db.delete(asset)
    db.commit()
    return {"message":"Asset deleted successfully"}
