from sqlalchemy.orm import Session
from models.user import User
from utils.security import verify_password, get_password_hash, create_access_token

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user is None or not verify_password(password, user.hashed_password):
        return False
    return user

def create_user(db: Session, username: str, password: str, email: str):
    hashed_password = get_password_hash(password)
    db_user = User(username=username, hashed_password=hashed_password, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
