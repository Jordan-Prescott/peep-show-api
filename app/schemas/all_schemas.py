from pydantic import BaseModel
from datetime import datetime


class Actor(BaseModel):
    first_name: str
    last_name: str
    gender: str
    participation_range: str
    total_episodes: int

    
class Audio(BaseModel):
    file_name: str
    file_type: str
    file_url: str    
    #TODO: FK


class Avatar(BaseModel):
    file_name: str
    file_type: str
    file_url: str
    #TODO: FK
    
    
class Character(BaseModel):
    first_name: str
    last_name: str
    first_appearance: str
    last_appearance: str
    total_episodes: int
    #TODO: FK
    
    
class Episode(BaseModel):
    title: str
    overall_episode_number: int
    episode_number: int
    air_date: datetime
    director: list[str]
    writers: list[str]
    synopsis: str
    #TODO: FK
    
    
class Line(BaseModel):
    line_number: int
    line_content: str
    spoken_by: str
    spoken_to: str
    #TODO: FK
    
    
class Location(BaseModel):
    name: str
    
    
class Meme(BaseModel):
    file_name: str
    file_type: str
    file_url: str


class Script(BaseModel):
    script_content: str
    writers: list[str]
    series: int
    episode: int
    
class Series(BaseModel):
    title: str
    description: str
    network: str
    premiere_date: datetime
    finale_date: datetime
    numnber_of_episodes: int