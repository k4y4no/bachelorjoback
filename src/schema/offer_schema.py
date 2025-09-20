from pydantic import BaseModel

class OfferCreate(BaseModel):
    name: str

class OfferResponse(OfferCreate):
    id: int

    class Config:
        from_attributes = True