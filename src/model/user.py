from src.config.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    firstname = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)
