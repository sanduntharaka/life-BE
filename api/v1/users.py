from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from services.user_service import authenticate_user, create_user
from schemas.user import UserCreate, Token
from utils.security import create_access_token
from core.db import get_db

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.password, user.email)
