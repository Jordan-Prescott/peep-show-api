import logging

from fastapi import APIRouter, HTTPException, Request
from typing import List

from ..db.supabase import SupabaseClient
from ..schemas.script import Script
from ..schemas.series import SeriesURLChoices
from ..schemas.episode import EpisodeURLChoices
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/scripts", tags=["scripts"])
db = SupabaseClient().get_client()
logger = logging.getLogger("app")

@router.get("/{series_number}/{episode_number}", response_model=List[Script])
@limiter.limit("5/second")
async def get_script(
    request: Request,
    series_number: SeriesURLChoices,
    episode_number: EpisodeURLChoices
    ) -> List[Script]:
    
    query = db.table("script").select(
        "series, episode, writers, script_content" 
    )
    
    query = query.eq("series", series_number.value)
    query = query.eq("episode", episode_number.value)
        
    try:
        response = query.execute()
    except Exception as e:
        logger.error(f"Query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Script not found")
    
    return [
        Script(**script) for script in response.data
    ]