from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.schema.user_schema import UserCreate, UserLogin
from src.service.auth_service import get_user_by_email
from src.config.hash import pwd_context
from src.model.user import User
from src.service.token_service import create_token


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
            "id_sub": db_user.id,
            "sub": user.email,
            "role": db_user.role
            })
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identifiants incorrects"

        )
