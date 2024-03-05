from datetime import datetime, timedelta
from typing import List

import requests

from src.domain.model.ohlc import OHLCModel
from src.domain.usecases.interfaces.ohlc_repository import IOHLCRepository
from src.main.config.settings import settings
from src.presentation.errors.generic_errors import GenericServerError


class OHLCRepository(IOHLCRepository):
    async def get(self, symbol: str) -> List[OHLCModel]:
        start_date = datetime(2012, 1, 1)
        end_date = datetime.now()

        final_data = []

        current_start = start_date
        while current_start < end_date:
            current_end = min(current_start + timedelta(days=90), end_date)

            segment_data = await self._get_batched_coin_data(
                product_id=symbol,
                start_date=current_start.isoformat(),
                end_date=current_end.isoformat(),
                granularity=86400,
            )

            final_data.extend(segment_data)

            current_start = current_end + timedelta(days=1)

        final_data.sort(key=lambda x: x.date)

        return final_data

    async def _get_batched_coin_data(
        self, product_id: str, start_date: str, end_date: str, granularity: int
    ) -> List[OHLCModel]:
        url = f"{settings.API_COIN_BASE_BASE_URL}/products/{product_id}/candles"
        params = {"start": start_date, "end": end_date, "granularity": granularity}

        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise GenericServerError("Error on getting OHLC data from external API")

        data = response.json()

        return [
            OHLCModel(
                date=datetime.fromtimestamp(row[0]),
                open=row[1],
                high=row[2],
                low=row[3],
                close=row[4],
            )
            for row in data
        ]
