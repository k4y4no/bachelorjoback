from src.config.database import Base
from sqlalchemy import Column, Integer, String

class Game:
    __tablename__ = "game"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)