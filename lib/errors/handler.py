from fastapi import FastAPI
from .not_found_error import NotFoundException, not_found_handler


def add_handlers(app: FastAPI):
    app.add_exception_handler(NotFoundException, not_found_handler)
