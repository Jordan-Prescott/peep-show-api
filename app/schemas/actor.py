from pydantic import BaseModel
from typing import Optional

class Actor(BaseModel):
    first_name: str
    last_name: str
    gender: Optional[str] = None
    participation_range: Optional[str] = None
    total_episodes: Optional[int] = None
    

class ActorCharacter(BaseModel):
    first_name: str
    last_name: str