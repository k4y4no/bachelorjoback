from pydantic import BaseModel

class GameCreate(BaseModel):
    name: str

class GameResponse(GameCreate):
    id: int

    class Config:
        from_attributes = True