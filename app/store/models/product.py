import sqlalchemy as sa
from lib.models import Base
from app.store.schemas import ProductCreateInput, ProductUpdateInput


class Product(Base):
    __tablename__ = 'product'

    title = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    amount = sa.Column(sa.Integer)
    price = sa.Column(sa.Float)

    def __init__(self, input: ProductCreateInput):
        self.title = input.title
        self.description = input.description
        self.amount = input.amount
        self.price = input.price

    def update(self, input: ProductUpdateInput):
        self.title = input.title
        self.description = input.description
        self.amount = input.amount
        self.price = input.price
