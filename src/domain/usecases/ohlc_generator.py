from src.domain.usecases.interfaces.ohlc_repository import IOHLCRepository


class OHLCGeneratorUsecase:
    def __init__(self, ohlc_repository: IOHLCRepository):
        self.ohlc_repository = ohlc_repository

    async def generate(self, symbol: str):
        ohlc = await self.ohlc_repository.get(symbol)
        return ohlc
