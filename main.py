from fastapi import FastAPI
from api.api import UserApi
from api.auth_api import AuthApi
from api.game_api import GameAPI
from api.offer_api import OfferAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.database import Base, engine

# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Api init
user_api = UserApi()
auth_api = AuthApi()
game_api = GameAPI()
offer_api = OfferAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    user_api.router,
    prefix="/user",
    tags=["User"]
)
app.include_router(
    auth_api.router,
    prefix="/auth",
    tags=["Auth"]
)
app.include_router(
    game_api.router,
    prefix="/game",
    tags=["Game"]
)
app.include_router(
    offer_api.router,
    prefix="/offer",
    tags=["Offer"]
)
