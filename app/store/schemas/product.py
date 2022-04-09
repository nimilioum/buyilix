import datetime

from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    description: str
    amount: int
    price: float

    class Config:
        orm_mode = True


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
