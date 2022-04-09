from fastapi import Depends
from db.config import get_session
from app.store.models import Product
from app.store.schemas import ProductCreateInput
from sqlalchemy.orm import Session


def from_create_input(data: ProductCreateInput) -> Product:
    return Product(title=data.title, description=data.description,
                   amount=data.amount, price=data.price)


class ProductService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self) -> list[Product]:
        return self.session.query(Product).all()

    def create(self, product_input: ProductCreateInput) -> Product:
        product = from_create_input(product_input)

        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)

        return product
