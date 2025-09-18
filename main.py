from fastapi import FastAPI
from api.api import UserApi
from fastapi.middleware.cors import CORSMiddleware
from src.config.database import Base, engine

# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Api init
user_api = UserApi()

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
