from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import List

from src.config.database import get_db
from src.controller.offer_controller import create_offer, read_offers, read_offer, update_offer, delete_offer
from src.schema.offer_schema import OfferCreate, OfferResponse
from src.service.token_service import verify_token

class OfferAPI:
    def __init__(self):
        self.router = APIRouter()
        self.add_routes()

    def add_routes(self):

        @self.router.post("/", response_model=OfferResponse)
        def create_offer_endpoint(offer: OfferCreate, request: Request, db: Session = Depends(get_db)):
            verify_token(request)
            return create_offer(offer, db)

        @self.router.get("/", response_model=List[OfferResponse])
        def read_offers_endpoint(db: Session = Depends(get_db)):
            return read_offers(db)

        @self.router.get("/{offer_id}", response_model=OfferResponse)
        def read_offer_endpoint(offer_id: int, db: Session = Depends(get_db)):
            return read_offer(offer_id, db)

        @self.router.put("/{offer_id}", response_model=OfferResponse)
        def update_offer_endpoint(offer_id: int, updated_offer: OfferCreate, request: Request, db: Session = Depends(get_db)):
            verify_token(request)
            return update_offer(offer_id, updated_offer, db)

        @self.router.delete("/{offer_id}", response_model=OfferResponse)
        def delete_offer_endpoint(offer_id: int, request: Request, db: Session = Depends(get_db)):
            verify_token(request)
            return delete_offer(offer_id, db)