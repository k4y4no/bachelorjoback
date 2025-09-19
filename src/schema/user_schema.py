from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str
class UserCreate(UserLogin):
    name: str
    firstname:str
    phone: str



class UserResponse(BaseModel):
    email: str
    name: str
    firstname:str
    phone: str
    id: int

    class Config:
        from_attributes = True