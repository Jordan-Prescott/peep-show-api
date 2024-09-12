from pydantic import BaseModel


class Line(BaseModel):
    line_number: int
    line_content: str
    spoken_by: str
    spoken_to: str
    #TODO: FK