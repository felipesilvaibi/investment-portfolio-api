from datetime import datetime

from pydantic import BaseModel


class OHLCModel(BaseModel):

    date: datetime
    low: float
    high: float
    open: float
    close: float
