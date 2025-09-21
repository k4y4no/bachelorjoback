from src.config.database import Base
from sqlalchemy import Column, Integer, String

class Offer(Base):
    __tablename__ = "offer"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    