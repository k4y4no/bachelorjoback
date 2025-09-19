from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.config.hash import pwd_context
from src.model.user import User
from src.service.auth_service import get_user_by_email
from src.service.token_service import create_token
from src.schema.user_schema import UserCreate, UserLogin


def create_user(user: UserCreate, db: Session):
    db_user = get_user_by_email(email=user.email, db=db)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This email is already used"
        )
    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        name=user.name,
        firstname=user.firstname,
        email=user.email,
        phone=user.phone,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


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

def login_user(user: UserLogin, db: Session):
    db_user = get_user_by_email(
        db=db,
        email=user.email
    )

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identifiants incorrects"
        )
    
    if pwd_context.verify(user.password, db_user.password): 
        return create_token(data={
            "sub": user.email,
            "role": db_user.role
            })
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identifiants incorrects"

        )
