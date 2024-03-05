from datetime import datetime
from enum import Enum
from typing import Dict, Union

from pydantic import BaseModel

from src.domain.usecases.interfaces.sync_client_notifier_adapter import (
    ISyncClientNotifierAdapter,
)
from src.infra.notifiers.sync_client_notifier_adapter import SyncClientNotifierInputDTO


class NotificationSenderUsecaseInputPort(BaseModel):
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


class NotificationSenderUsecase:
    def __init__(self, notifier: ISyncClientNotifierAdapter):
        self.notifier = notifier

    def send(self, message: NotificationSenderUsecaseInputPort) -> None:

        message = SyncClientNotifierInputDTO(
            type=message.type,
            recipient_id=message.recipient_id,
            message_type=message.message_type,
            message=message.message,
        )
        self.notifier.notify(message)
