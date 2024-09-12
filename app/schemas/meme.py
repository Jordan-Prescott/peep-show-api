from pydantic import BaseModel


class Meme(BaseModel):
    file_name: str
    file_type: str
    file_url: str
