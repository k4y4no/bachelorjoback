from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./jo2024.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False}
)

session_local = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    )

Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close