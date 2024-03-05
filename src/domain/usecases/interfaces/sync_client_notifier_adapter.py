from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Dict, Union

from pydantic import BaseModel


class SyncClientNotifierInputDTO(BaseModel):
    class NotificationType(str, Enum):
        TELEGRAM = "TELEGRAM"

    class MessageType(str, Enum):
        GENERIC = "GENERIC"
        TRADE = "TRADE"

    class GenericMessage(BaseModel):
        content: str

    class TradeMessage(BaseModel):
        class TradeAction(str, Enum):
            BUY = "BUY"
            SELL = "SELL"
            HOLD = "HOLD"

        trade_action: TradeAction
        indicators: Dict[str, Union[str, int, float, bool, datetime]]

    type: NotificationType
    recipient_id: str
    message_type: MessageType
    message: Union[GenericMessage, TradeMessage]


class ISyncClientNotifierAdapter(ABC):

    @abstractmethod
    def notify(self, message: SyncClientNotifierInputDTO) -> None:
        pass
