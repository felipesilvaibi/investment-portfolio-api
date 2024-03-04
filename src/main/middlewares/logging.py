import base64
import json
import random
import string
from typing import Callable, Tuple

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from src.main.config.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request_id = request.headers.get("X-Request-ID", self._generate_random_id())

        request_params, is_topic_message = await self._extract_request_parameters(
            request
        )

        with logger.contextualize(request_id=request_id):
            logger.info(f"Request {request.method}: {request.url.path}")

            if is_topic_message:
                logger.debug(f"Decoded Topic Message Payload: {request_params}")
            else:
                logger.debug(f"Payload: {request_params}")

            return await call_next(request)

    async def _extract_request_parameters(self, request: Request) -> Tuple[str, bool]:
        if request.method == "GET":
            query_params = dict(request.query_params)
            path_params = request.path_params
            return {**query_params, **path_params}, False
        else:
            body_bytes = await request.body()
            body = body_bytes.decode()

            try:
                body_json = json.loads(body)
                if "message" in body_json and "data" in body_json["message"]:
                    data = body_json["message"]["data"]
                    decoded_data = base64.b64decode(data).decode("utf-8")
                    return json.loads(decoded_data), True
            except json.decoder.JSONDecodeError:
                pass

            return body, False

    def _generate_random_id(self, length: int = 6) -> str:
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))
