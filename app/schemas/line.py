from pydantic import BaseModel
from typing import Optional

from .location import Location
from .meme import Meme


class LineScript(BaseModel):
    series: int
    episode: int


class Line(BaseModel):
    line_content: str
    spoken_by: str
    spoken_to: str
    script: Optional[LineScript]
    line_number: int
    location: Optional[Location]
    meme_metadata: Optional[Meme] = None
    
    
class LineFilter(BaseModel):
    spoken_by: str
    spoken_to: str
    line_content: str