from fastapi import APIRouter, Depends
from starlette.status import HTTP_204_NO_CONTENT

from app.store.services import ProductService
from app.store.schemas import ProductListModel, ProductReadModel, ProductCreateInput, ProductUpdateInput

router = APIRouter(
    prefix="/products"
)


@router.get('/', response_model=list[ProductListModel])
async def get_all(service: ProductService = Depends(ProductService)):
    return service.get_all()


@router.get('/{id}', response_model=ProductReadModel)
async def find(id: int, service: ProductService = Depends(ProductService)):
    return service.find(id)


@router.post('/', response_model=ProductReadModel)
async def create(product_input: ProductCreateInput, service: ProductService = Depends(ProductService)):
    product = service.create(product_input)
    return product


@router.put('/{id}', response_model=ProductReadModel)
async def update(id: int, product_input: ProductUpdateInput, service: ProductService = Depends(ProductService)):
    return service.update(id, product_input)


@router.delete('/{id}', response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete(id: int, service: ProductService = Depends(ProductService)):
    return service.delete(id)
