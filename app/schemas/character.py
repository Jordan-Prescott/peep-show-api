from pydantic import BaseModel
from typing import Optional

from .actor import ActorCharacter

class Character(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    first_appearance: str
    last_appearance: str
    total_episodes: int
    actor: Optional[ActorCharacter] = None
    
class CharacterAudio(BaseModel):
    first_name: str
    last_name: str