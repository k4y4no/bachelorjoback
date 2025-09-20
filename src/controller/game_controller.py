from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.schema.game_schema import GameCreate
from src.model.game import Game

def create_game(game: GameCreate, db: Session):
    new_game: Game = Game(**game.model_dump())
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game

# Lire tous les films
def read_games(db: Session):
    return db.query(Game).all()

# Lire un film par ID
def read_game(game_id: int, db: Session):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

# Mettre à jour un film
def update_game(game_id: int, updated_game: GameCreate, db: Session):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    for key, value in updated_game.dict().items():
        setattr(game, key, value)
    db.commit()
    db.refresh(game)
    return game

# Supprimer un film
def delete_game(game_id: int, db: Session):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete(game)
    db.commit()
    return game