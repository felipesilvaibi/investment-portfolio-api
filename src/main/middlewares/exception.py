from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.main.config.logger import logger
from src.presentation.errors.generic_errors import (
    GenericClientError,
    GenericServerError,
)


def bad_request(error: str, status_code: int = 400) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"error": error})


def server_error(error: str, status_code: int = 500) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"error": error})


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> JSONResponse:
        try:
            return await call_next(request)
        except GenericClientError as gen_client_error:
            error = gen_client_error.args[0]

            if gen_client_error.args[1] is not None:
                detailed_error = f"{error}: {gen_client_error.args[1]}"
            else:
                detailed_error = error

            logger.warning(detailed_error)
            return bad_request(error)
        except GenericServerError as gen_server_error:
            error = gen_server_error.args[0]

            if gen_server_error.args[1] is not None:
                detailed_error = f"{error}: {gen_server_error.args[1]}"
            else:
                detailed_error = error

            logger.error(detailed_error)
            return server_error(error)
        except Exception as e:
            logger.error(e)
            return server_error("Internal server error")
