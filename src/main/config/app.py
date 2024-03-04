from fastapi import FastAPI

from src.main.config.middlewares import setup_middlewares
from src.main.config.routes import setup_routes

app = FastAPI(docs_url="/docs")

setup_middlewares(app)
setup_routes(app)
