from pydantic import BaseModel
from typing import List
from datetime import datetime
from enum import Enum

class EpisodeURLChoices(Enum):
    EPISODE_1 = '1'
    EPISODE_2 = '2'
    EPISODE_3 = '3'
    EPISODE_4 = '4'
    EPISODE_5 = '5'
    EPISODE_6 = '6'

class Episode(BaseModel):
    title: str
    overall_episode_number: int
    episode_number: int
    air_date: datetime
    directors: str
    writers: str
    synopsis: str
    #TODO: FK