from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class SeriesURLChoices(Enum):
    SERIES_1 = '1'
    SERIES_2 = '2'
    SERIES_3 = '3'
    SERIES_4 = '4'
    SERIES_5 = '5'
    SERIES_6 = '6'
    SERIES_7 = '7'
    SERIES_8 = '8'
    SERIES_9 = '9'

class Series(BaseModel):
    title: str
    description: str
    network: str
    premier_date: datetime
    finale_date: datetime
    number_of_episodes: int
    