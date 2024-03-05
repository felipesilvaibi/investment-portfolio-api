import requests

from src.domain.usecases.interfaces.sync_client_notifier_adapter import (
    ISyncClientNotifierAdapter,
    SyncClientNotifierInputDTO,
)
from src.main.config.settings import settings
from src.presentation.errors.generic_errors import GenericServerError


class SyncClientNotifierAdapter(ISyncClientNotifierAdapter):

    async def notify(self, message: SyncClientNotifierInputDTO) -> None:
        url = settings.NOTIFICATION_CLIENT_URL

        requests.post(url, json=message.model_dump())

        response = self.client.send(message)
        if response.status_code != 200:
            raise GenericServerError("Error on sending notification to external API")
