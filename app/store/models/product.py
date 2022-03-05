from sqlmodel import SQLModel, Field
from pydantic import validator, ValidationError


class ProductBase(SQLModel):
    title: str
    description: str
    amount: int
    price: float


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    # @validator('amount')
    # def amount_validator(cls, v: int):
    #     if v < 0:
    #         return ValidationError("amount cannot be less than zero")
    #
    # @validator('price')
    # def price_validator(cls, v: float):
    #     if v < 0:
    #         return ValidationError("price cannot be less than zero")
