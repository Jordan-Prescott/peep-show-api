from pydantic import BaseModel


class Script(BaseModel):
    script_content: str
    writers: list[str]
    series: int
    episode: int