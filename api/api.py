from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.schema.user_schema import UserCreate, UserResponse
from src.controller.user_controller import read_users, create_user, read_user_by_id, delete_user, update_user

class UserApi:
    def __init__(self):
        self.router = APIRouter()
        self.add_routes()

    def add_routes(self):

        @self.router.post(path="/", response_model=UserResponse)
        def create_user_endpoint(user:UserCreate, db: Session = Depends(get_db)):
            return create_user(user, db)
        
        @self.router.get(path="/", response_model=list[UserResponse])
        def read_users_endpoint(db: Session = Depends(get_db)):
            return read_users(db)
        
        @self.router.get(path="/{user_id}", response_model=UserResponse)
        def read_users_by_id__endpoint(user_id:int, db: Session = Depends(get_db)):
            return read_user_by_id(user_id, db)
        
        @self.router.delete(path="/{user_id}", response_model=UserResponse)
        def delete_user__endpoint(user_id:int, db: Session = Depends(get_db)):
            return delete_user(user_id, db)
        
        @self.router.put(path="/{user_id}", response_model=UserResponse)
        def update_user__endpoint(user_id:int, updated_user: UserCreate, db: Session = Depends(get_db)):
            return update_user(user_id, updated_user, db)