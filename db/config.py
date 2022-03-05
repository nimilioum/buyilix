import os
from sqlmodel import create_engine, Session
from dotenv import load_dotenv

load_dotenv()
PG_USER = os.environ['PG_USER']
PG_PASS = os.environ['PG_PASS']
PG_HOST = os.environ['PG_HOST']
PG_DATABASE = os.environ['PG_DATABASE']

POSTGRES_DATABASE_URL = f'postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}/{PG_DATABASE}'\

engine = create_engine(POSTGRES_DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session



