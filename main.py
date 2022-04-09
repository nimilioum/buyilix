from fastapi import FastAPI
from dotenv import load_dotenv
from routers import store
from db.migrate import migrate
from db.config import engine
from lib.errors import add_handlers

load_dotenv()
migrate(engine)

app = FastAPI()

app.include_router(store.get_router())
add_handlers(app)
