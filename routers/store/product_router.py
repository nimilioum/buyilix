from fastapi import APIRouter, Depends
from app.store.services import ProductService
from app.store.schemas import ProductListModel, ProductReadModel, ProductCreateInput

router = APIRouter(
    prefix="/product"
)


@router.get('/', response_model=list[ProductListModel])
async def get_all(service: ProductService = Depends(ProductService)):
    return service.get_all()


@router.post('/', response_model=ProductReadModel)
async def create(product_input: ProductCreateInput, service: ProductService = Depends(ProductService)):
    product = service.create(product_input)
    return product
