from datetime import datetime
from enum import Enum, auto
from typing import List

import numpy as np
import pandas as pd

from src.domain.model.ohlc import OHLCModel
from src.presentation.errors.generic_errors import GenericServerError


class RsiCalculatorTemporalWindow(str, Enum):
    WEEKLY = auto()
    MONTHLY = auto()


class RsiCalculatorUsecase:

    def get_today_rsi(
        self, ohlc: List[OHLCModel], temporal_window: RsiCalculatorTemporalWindow
    ):
        ohlc_df = self._convert_ohlc_models_to_df(ohlc)
        ohlc_df = self._set_date_index(ohlc_df)
        resampled_ohlc = self._resample_ohlc(ohlc_df, temporal_window)
        rsi = self._calculate_tv_rsi(resampled_ohlc)

        return self._get_today_rsi(rsi)

    def _convert_ohlc_models_to_df(self, ohlc_models):
        data = [
            {
                "date": model.date,
                "low": model.low,
                "high": model.high,
                "open": model.open,
                "close": model.close,
            }
            for model in ohlc_models
        ]
        return pd.DataFrame(data)

    def _set_date_index(self, ohlc_df):
        ohlc_df["date"] = pd.to_datetime(ohlc_df["date"])
        ohlc_df.set_index("date", inplace=True)
        return ohlc_df

    def _resample_ohlc(self, ohlc_df, temporal_window):
        if temporal_window == RsiCalculatorTemporalWindow.WEEKLY:
            resampled_ohlc = ohlc_df.resample("W").last()
        elif temporal_window == RsiCalculatorTemporalWindow.MONTHLY:
            resampled_ohlc = ohlc_df.resample("M").last()
        else:
            raise GenericServerError("Temporal window not supported")
        return resampled_ohlc

    def _calculate_tv_rsi(self, ohlc_df):
        delta = ohlc_df["close"].diff()

        default_period = 14

        up = delta.copy()
        up[up < 0] = 0
        up = pd.Series.ewm(up, alpha=1 / default_period, adjust=False).mean()

        down = delta.copy()
        down[down > 0] = 0
        down *= -1
        down = pd.Series.ewm(down, alpha=1 / default_period, adjust=False).mean()

        rsi = np.where(
            up == 0, 0, np.where(down == 0, 100, 100 - (100 / (1 + up / down)))
        )
        ohlc_df["RSI"] = np.round(rsi, 2)
        return ohlc_df

    def _get_today_rsi(self, ohlc_df):
        today = datetime.today().date()
        if today in ohlc_df.index:
            return ohlc_df.loc[today, "RSI"]
        else:
            return None
