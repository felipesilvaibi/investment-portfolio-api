from abc import ABC, abstractmethod
from typing import List

from src.domain.model.ohlc import OHLCModel


class IOHLCRepository(ABC):

    @abstractmethod
    async def get(self, symbol: str) -> List[OHLCModel]:
        pass
