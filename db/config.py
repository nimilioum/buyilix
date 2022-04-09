import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


load_dotenv()
PG_USER = os.environ['PG_USER']
PG_PASS = os.environ['PG_PASS']
PG_HOST = os.environ['PG_HOST']
PG_DATABASE = os.environ['PG_DATABASE']

POSTGRES_DATABASE_URL = f'postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}/{PG_DATABASE}'

engine = create_engine(POSTGRES_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
