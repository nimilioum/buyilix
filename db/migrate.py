from sqlmodel import SQLModel

from app.store.models import Product


def migrate(engine):
    SQLModel.metadata.create_all(engine)
