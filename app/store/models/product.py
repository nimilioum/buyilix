import sqlalchemy as sa
from lib.models import Base


# ss
# @validator('amount')
# def amount_validator(cls, v: int):
#     if v < 0:
#         return ValidationError("amount cannot be less than zero")
#
# @validator('price')
# def price_validator(cls, v: float):
#     if v < 0:
#         return ValidationError("price cannot be less than zero")


class Product(Base):
    __tablename__ = 'product'

    title = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    amount = sa.Column(sa.Integer)
    price = sa.Column(sa.Float)
