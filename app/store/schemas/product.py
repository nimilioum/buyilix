import datetime
from pydantic import BaseModel, validator


class ProductBase(BaseModel):
    title: str
    description: str
    amount: int
    price: float

    class Config:
        orm_mode = True

    @validator('amount')
    def amount_positive_integer(cls, v: int):
        if v < 0:
            raise ValueError("amount cannot be less than zero")
        return v

    @validator('price')
    def price_positive_float(cls, v: float):
        if v < 0:
            raise ValueError("price cannot be less than zero")
        return v


class ProductCreateInput(ProductBase):
    pass


class ProductUpdateInput(ProductBase):
    pass


class ProductReadModel(ProductBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ProductListModel(ProductReadModel):
    pass
