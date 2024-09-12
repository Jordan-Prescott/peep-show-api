from pydantic import BaseModel


class Audio(BaseModel):
    file_name: str
    file_type: str
    file_url: str    
    #TODO: FK