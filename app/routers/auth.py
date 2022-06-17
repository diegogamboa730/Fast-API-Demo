#Modules
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.orm import Session #imports database session 
from .. import models,schemas,utils,oath2
from ..database import get_db 

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login",response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    
    #Token creation
    access_token = oath2.create_access_token(data= {"user_id": user.id})
    return {"access_token":access_token, "token_type":"bearer"}

