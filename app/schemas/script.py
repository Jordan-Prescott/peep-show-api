from pydantic import BaseModel
from enum import Enum

class URLChoices(Enum):
    SERIES_1 = '1'
    SERIES_2 = '2'
    SERIES_3 = '3'
    SERIES_4 = '4'
    SERIES_5 = '5'
    SERIES_6 = '6'
    SERIES_7 = '7'
    SERIES_8 = '8'
    SERIES_9 = '9'

class Script(BaseModel):
    series: int
    episode: int
    writers: str
    script_content: str