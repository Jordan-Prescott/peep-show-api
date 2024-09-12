from pydantic import BaseModel
from datetime import datetime



class Episode(BaseModel):
    title: str
    overall_episode_number: int
    episode_number: int
    air_date: datetime
    director: list[str]
    writers: list[str]
    synopsis: str
    #TODO: FK