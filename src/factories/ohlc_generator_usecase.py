from src.domain.usecases.ohlc_generator import OHLCGeneratorUsecase
from src.infra.external_db.ohlc_repository import OHLCRepository


def make_ohlc_generator_usecase() -> OHLCGeneratorUsecase:
    return OHLCGeneratorUsecase(
        ohlc_repository=OHLCRepository(),
    )
