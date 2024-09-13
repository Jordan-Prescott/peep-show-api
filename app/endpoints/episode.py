from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime

from ..db.supabase import SupabaseClient
from ..schemas.episode import Episode, EpisodeURLChoices
from ..schemas.series import SeriesURLChoices

router = APIRouter(prefix="/episodes", tags=["episodes"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Episode])
async def get_episodes(
    title: Optional[str] = Query(None, example="Warring Factions"),
    start_date: Optional[str] = Query(None, example="2005-09-21"),
    end_date: Optional[str] = Query(None, example="2006-10-12"),
    ) -> List[Episode]:
    
    query = db.table("episode").select(
        "title, overall_episode_number, episode_number, air_date, \
            directors, writers, synopsis, series(number)"
    )

    if title:
        title = title.capitalize()
        query = query.like("title", f"%{title}%")

    if start_date:
        try:
            start_date_parsed = datetime.strptime(start_date, "%Y-%m-%d")
            query = query.gte("air_date", start_date_parsed.strftime("%Y-%m-%d"))
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid start date format. Use YYYY-MM-DD.")

    if end_date:
        try:
            end_date_parsed = datetime.strptime(end_date, "%Y-%m-%d")
            query = query.lte("air_date", end_date_parsed.strftime("%Y-%m-%d"))
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid end date format. Use YYYY-MM-DD.")
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Episode not found")
    
    return [
        Episode(**episode) for episode in response.data
    ]