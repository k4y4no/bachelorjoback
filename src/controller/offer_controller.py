from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.schema.offer_schema import OfferCreate
from src.model.offer import Offer

def create_offer(offer: OfferCreate, db: Session):
    new_offer: Offer = Offer(**offer.model_dump())
    db.add(new_offer)
    db.commit()
    db.refresh(new_offer)
    return new_offer

# Lire tous les films
def read_offers(db: Session):
    return db.query(Offer).all()

# Lire un film par ID
def read_offer(offer_id: int, db: Session):
    offer = db.query(Offer).filter(Offer.id == offer_id).first()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer

# Mettre à jour un film
def update_offer(offer_id: int, updated_offer: OfferCreate, db: Session):
    offer = db.query(Offer).filter(Offer.id == offer_id).first()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    for key, value in updated_offer.dict().items():
        setattr(offer, key, value)
    db.commit()
    db.refresh(offer)
    return offer

# Supprimer un film
def delete_offer(offer_id: int, db: Session):
    offer = db.query(Offer).filter(Offer.id == offer_id).first()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    db.delete(offer)
    db.commit()
    return offer