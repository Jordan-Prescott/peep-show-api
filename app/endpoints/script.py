from fastapi import APIRouter, HTTPException
from typing import List

from ..db.supabase import SupabaseClient
from ..schemas.script import Script
from ..schemas.series import SeriesURLChoices
from ..schemas.episode import EpisodeURLChoices

router = APIRouter(prefix="/scripts", tags=["scripts"])

db = SupabaseClient().get_client()

@router.get("/{series_number}/{episode_number}", response_model=List[Script])
async def get_script(
    series_number: SeriesURLChoices,
    episode_number: EpisodeURLChoices
    ) -> List[Script]:
    
    query = db.table("script").select(
        "series, episode, writers, script_content" 
    )
    
    query = query.eq("series", series_number.value)
    query = query.eq("episode", episode_number.value)
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Script not found")
    
    return [
        Script(**script) for script in response.data
    ]