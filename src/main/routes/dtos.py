import base64
import json
from typing import Any

from pydantic import BaseModel


class InputDTO(BaseModel):
    def __init__(__pydantic_self__, **data: Any):
        if 'message' in data and 'data' in data['message']:
            try:
                encoded_data = data['message']['data']
                decoded_data = base64.b64decode(encoded_data).decode('utf-8')
                message_data = json.loads(decoded_data)

                data = message_data
            except (ValueError, json.JSONDecodeError):
                pass

        super().__init__(**data)


class OutputDTO(BaseModel):
    pass
