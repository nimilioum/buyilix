import sqlalchemy as sa
from lib.models import Base


class Product(Base):
    __tablename__ = 'product'

    title = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    amount = sa.Column(sa.Integer)
    price = sa.Column(sa.Float)
