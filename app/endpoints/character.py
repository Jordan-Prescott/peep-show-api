from fastapi import APIRouter, HTTPException
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.character import Character
from ..schemas.episode import CharacterEpisode

router = APIRouter(prefix="/characters", tags=["character"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Character])
async def get_characters(
    first_name: Optional[str] = None,
    last_name: Optional[str] = None
    ) -> List[Character]:
    
    query = db.table("character").select(
        "first_name, last_name, first_appearance, last_appearance, total_episodes"
    )

    if first_name:
        first_name = first_name.capitalize()
        query = query.like("first_name", f"%{first_name}%")
    if last_name:
        last_name = last_name.capitalize()
        query = query.like("last_name", f"%{last_name}%")
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Character not found")
    
    return [
        Character(**character) for character in response.data
    ]
    
@router.get("/episode/", response_model=List[CharacterEpisode])
async def get_characters(
    episode_title: Optional[str] = None,
    series_number: Optional[int] = None
    ) -> List[CharacterEpisode]:
    
    query = db.table("character_episode").select(
        "character(first_name, last_name), episode(title, series(number))"
    )

    if series_number:
        query = query.like("episode.series.number", series_number)
        
    response = query.execute()
    
    print(response.data)
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Episodes not found")
    
    return [
        CharacterEpisode(**episode["episode"]) for episode in response.data if episode["character"] is not None
    ]