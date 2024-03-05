from src.domain.usecases.rsi_calculator import RsiCalculatorUsecase
from src.factories.notification_sender_usecase import make_notification_sender_usecase
from src.factories.ohlc_generator_usecase import make_ohlc_generator_usecase
from src.presentation.controllers.trade_action_report_generator import (
    TradeActionReportGeneratorController,
)


def make_trade_action_report_generator_controller() -> (
    TradeActionReportGeneratorController
):
    return TradeActionReportGeneratorController(
        ohlc_generator=make_ohlc_generator_usecase(),
        rsi_calculator=RsiCalculatorUsecase(),
        notification_sender=make_notification_sender_usecase(),
    )
