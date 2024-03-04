from fastapi import FastAPI

from src.main.middlewares.cors import CORSMiddleware
from src.main.middlewares.exception import ExceptionMiddleware
from src.main.middlewares.logging import LoggingMiddleware


def setup_middlewares(app: FastAPI):
    app.add_middleware(CORSMiddleware)
    app.add_middleware(ExceptionMiddleware)
    app.add_middleware(LoggingMiddleware)
