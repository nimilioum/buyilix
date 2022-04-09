from fastapi import Depends
from sqlalchemy.orm import Session
from db.config import get_session
from app.store.models import Product
from app.store.schemas import ProductCreateInput, ProductUpdateInput
from lib.errors import NotFoundException


class ProductService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self) -> list[Product]:
        return self.session.query(Product).all()

    def find(self, id: int) -> Product:
        return self.get_or_not_found(id)

    def create(self, product_input: ProductCreateInput) -> Product:
        product = Product(product_input)

        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)

        return product

    def update(self, id: int, product_input: ProductUpdateInput) -> Product:
        product: Product = self.session.query(Product).get(id)
        product.update(product_input)
        self.session.commit()
        self.session.refresh(product)
        return product

    def delete(self, id: int) -> None:
        product: Product = self.get_or_not_found(id)
        self.session.delete(product)
        self.session.commit()

    def get_or_not_found(self, id: int) -> Product:
        product: Product = self.session.query(Product).get(id)
        if product:
            return product
        else:
            raise NotFoundException(f"product with id {id} not found")
