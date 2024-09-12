from pydantic import BaseModel

class Actor(BaseModel):
    first_name: str
    last_name: str
    gender: str
    participation_range: str
    total_episodes: int