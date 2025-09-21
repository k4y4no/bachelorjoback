from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import List

from src.config.database import get_db
from src.controller.game_controller import create_game, read_games, read_game, update_game, delete_game
from src.schema.game_schema import GameCreate, GameResponse
from src.service.token_service import verify_token

class GameAPI:
    def __init__(self):
        self.router = APIRouter()
        self.add_routes()

    def add_routes(self):

        @self.router.post("/", response_model=GameResponse)
        def create_game_endpoint(game: GameCreate, request: Request, db: Session = Depends(get_db)):
            # verify_token(request)
            return create_game(game, db)

        @self.router.get("/", response_model=List[GameResponse])
        def read_games_endpoint(db: Session = Depends(get_db)):
            return read_games(db)

        @self.router.get("/{game_id}", response_model=GameResponse)
        def read_game_endpoint(game_id: int, db: Session = Depends(get_db)):
            return read_game(game_id, db)

        @self.router.put("/{game_id}", response_model=GameResponse)
        def update_game_endpoint(game_id: int, updated_game: GameCreate, request: Request, db: Session = Depends(get_db)):
            # verify_token(request)
            return update_game(game_id, updated_game, db)

        @self.router.delete("/{game_id}", response_model=GameResponse)
        def delete_game_endpoint(game_id: int, request: Request, db: Session = Depends(get_db)):
            # verify_token(request)
            return delete_game(game_id, db)