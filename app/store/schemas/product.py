from app.store.models import ProductBase


class ProductCreateInput(ProductBase):
    pass


class ProductUpdateInput(ProductBase):
    pass


class ProductReadModel(ProductBase):
    id: int


class ProductListModel(ProductBase):
    id: int