from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    firstname:str
    email: str
    phone: str
    password: str


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True