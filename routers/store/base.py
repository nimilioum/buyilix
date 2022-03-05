from fastapi import APIRouter
from .product_router import router as product_router


def get_router():
    router = APIRouter(
        prefix="/store"
    )

    router.include_router(product_router)

    return router
