from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.model_1 import Base

DATABASE_URL = "sqlite:///inventory.db"

def get_engine():
    return create_engine(DATABASE_URL)

def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

















