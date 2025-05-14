from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#DATABASE_URL = "postgresql://postgres:2304@localhost:5432/INDOOR_SYSTEM" # TODO
DATABASE_URL = os.getenv("DATABASE_URL")

db_engine = create_engine(DATABASE_URL)
DBSession = sessionmaker(
    bind=db_engine, 
    autocommit=False, 
    autoflush=False
)
ORMBaseModel = declarative_base()

def get_db_session():
    db_session = DBSession()
    try:
        yield db_session 
    finally:
        db_session.close()
