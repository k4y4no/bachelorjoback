from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.config.hash import pwd_context
from src.model.user import User
from src.service.auth_service import get_user_by_email
from src.service.token_service import create_token
from src.schema.user_schema import UserCreate, UserLogin


def read_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,
                            detail="User not found")
    
    return user

def read_users(db: Session):
    return db.query(User).all()

def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,
                            detail="User not found")
    
    db.delete(user)
    db.commit()
    return user

def update_user(user_id: int, updated_user: UserCreate,db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,
                            detail="User not found")
    
    for key, value in updated_user.model_dump().items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user

