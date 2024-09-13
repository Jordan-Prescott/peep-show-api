from pydantic import BaseModel
from typing import Optional

from .character import CharacterAudio

class Audio(BaseModel):
    file_name: str
    file_type: str
    file_url: str
    character: Optional[CharacterAudio] = None