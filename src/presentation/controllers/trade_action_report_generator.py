from src.domain.usecases.notification_sender import (
    NotificationSenderUsecase,
    NotificationSenderUsecaseInputPort,
)
from src.domain.usecases.ohlc_generator import OHLCGeneratorUsecase
from src.domain.usecases.rsi_calculator import (
    RsiCalculatorTemporalWindow,
    RsiCalculatorUsecase,
)
from src.main.config.settings import settings
from src.presentation.errors.generic_errors import GenericServerError


class TradeActionReportGeneratorController:
    def __init__(
        self,
        ohlc_generator: OHLCGeneratorUsecase,
        rsi_calculator: RsiCalculatorUsecase,
        notification_sender: NotificationSenderUsecase,
    ):
        self.ohlc_generator = ohlc_generator
        self.rsi_calculator = rsi_calculator
        self.notification_sender = notification_sender

    async def handle(self) -> str:
        ohlc = await self.ohlc_generator.generate("BTC-USD")

        monthly_rsi = self.rsi_calculator.get_today_rsi(
            ohlc, RsiCalculatorTemporalWindow.MONTHLY
        )
        if monthly_rsi is None:
            raise GenericServerError("Error on getting monthly RSI")

        weekly_rsi = self.rsi_calculator.get_today_rsi(
            ohlc, RsiCalculatorTemporalWindow.WEEKLY
        )
        if weekly_rsi is None:
            raise GenericServerError("Error on getting weekly RSI")

        trade_action = self._get_trade_action(monthly_rsi, weekly_rsi)

        await self._send_notification(trade_action, monthly_rsi, weekly_rsi)

    def _get_trade_action(
        self, monthly_rsi: float, weekly_rsi: float
    ) -> NotificationSenderUsecaseInputPort.TradeMessage.TradeAction:
        possible_trade_actions = (
            NotificationSenderUsecaseInputPort.TradeMessage.TradeAction
        )

        if monthly_rsi < 50 and weekly_rsi < 37:
            trade_action = possible_trade_actions.BUY
        elif monthly_rsi > 70 and weekly_rsi < 78:
            trade_action = possible_trade_actions.SELL
        else:
            trade_action = possible_trade_actions.HOLD

        return trade_action

    async def _send_notification(
        self, trade_action: str, monthly_rsi: float, weekly_rsi: float
    ):
        await self.notification_sender.send(
            NotificationSenderUsecaseInputPort(
                type=NotificationSenderUsecaseInputPort.NotificationType.TELEGRAM,
                recipient_id=settings.NOTIFICATION_RECIPIENT_ID,
                message_type=NotificationSenderUsecaseInputPort.MessageType.TRADE,
                message=NotificationSenderUsecaseInputPort.TradeMessage(
                    trade_action=trade_action,
                    indicators={"monthly_rsi": monthly_rsi, "weekly_rsi": weekly_rsi},
                ),
            )
        )
