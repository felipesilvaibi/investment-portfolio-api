from src.domain.usecases.notification_sender import NotificationSenderUsecase
from src.infra.notifiers.sync_client_notifier_adapter import SyncClientNotifierAdapter


def make_notification_sender_usecase() -> NotificationSenderUsecase:
    return NotificationSenderUsecase(
        notifier=SyncClientNotifierAdapter(),
    )
