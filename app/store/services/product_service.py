from sqlmodel import Session, select
from fastapi import Depends
from db.config import get_session
from app.store.models import Product
from app.store.schemas import ProductCreateInput


class ProductService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self) -> list[Product]:
        return self.session.exec(select(Product)).all()

    def create(self, product_input: ProductCreateInput) -> Product:
        product = Product.from_orm(product_input)

        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)

        return product
