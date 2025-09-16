from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    password: str

class UserCreate(UserBase):
    name: str
    firstname:str
    phone: str



class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True