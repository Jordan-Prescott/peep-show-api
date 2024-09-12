from pydantic import BaseModel
from datetime import datetime

class SeriesURLChoices(BaseModel):
    SERIES_1 = 'series1'
    SERIES_2 = 'series2'
    SERIES_3 = 'series3'
    SERIES_4 = 'series4'
    SERIES_5 = 'series5'
    SERIES_6 = 'series6'
    SERIES_7 = 'series7'
    SERIES_8 = 'series8'
    SERIES_9 = 'series9'

class Series(BaseModel):
    title: str
    description: str
    network: str
    premiere_date: datetime
    finale_date: datetime
    number_of_episodes: int
    