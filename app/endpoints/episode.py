import logging

from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional
from datetime import datetime

from ..db.supabase import SupabaseClient
from ..schemas.episode import Episode
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/episodes", tags=["episodes"])
db = SupabaseClient().get_client()
logger = logging.getLogger("app")

@router.get("/", response_model=List[Episode])
@limiter.limit("5/second")
async def get_episodes(
    request: Request,
    title: Optional[str] = Query(None, example="Warring Factions"),
    start_date: Optional[str] = Query(None, example="2003-09-19"),
    end_date: Optional[str] = Query(None, example="2003-09-19"),
    ) -> List[Episode]:
    
    query = db.table("episode").select(
        "title, overall_episode_number, episode_number, air_date, \
            directors, writers, synopsis, series(number)"
    )

    if title:
        title = title.capitalize()
        query = query.ilike("title", f"%{title}%")

    if start_date:
        try:
            start_date_parsed = datetime.strptime(start_date, "%Y-%m-%d")
            query = query.gte("air_date", start_date_parsed.strftime("%Y-%m-%d"))
            logger.info(f"Searching for episodes aired after: {start_date}")
        except ValueError:
            logging.error(f"Invalid start date format: {start_date}")
            raise HTTPException(status_code=400, detail="Invalid start date format. Use YYYY-MM-DD.")

    if end_date:
        try:
            end_date_parsed = datetime.strptime(end_date, "%Y-%m-%d")
            query = query.lte("air_date", end_date_parsed.strftime("%Y-%m-%d"))
            logger.info(f"Searching for episodes aired before: {end_date}")
        except ValueError:
            logging.error(f"Invalid end date format: {end_date}")
            raise HTTPException(status_code=400, detail="Invalid end date format. Use YYYY-MM-DD.")
    
    try:
        response = query.execute()
    except Exception as e:
        logger.error(f"query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Episode not found")
    
    return [
        Episode(**episode) for episode in response.data
    ]