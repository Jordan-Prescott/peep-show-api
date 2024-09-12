from pydantic import BaseModel


class Character(BaseModel):
    first_name: str
    last_name: str
    first_appearance: str
    last_appearance: str
    total_episodes: int
    #TODO: FK