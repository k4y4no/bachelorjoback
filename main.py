from fastapi import FastAPI
from api.api import UserApi
from src.config.database import Base, engine

# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Api init
user_api = UserApi()

app.include_router(
    user_api.router,
    prefix="/user",
    tags=["User"]
)
