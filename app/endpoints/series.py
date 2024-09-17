import logging

from fastapi import APIRouter, HTTPException, Request
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.series import Series, SeriesURLChoices
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/series", tags=["series"])
db = SupabaseClient().get_client()
logger = logging.getLogger("app")

@router.get("/", response_model=List[Series])
@limiter.limit("5/second")
async def get_series(
    request: Request,
    series_number: Optional[SeriesURLChoices] | None = None
    ) -> List[Series]:
    
    query = db.table("series").select(
        "title, description, network, premier_date, finale_date, number_of_episodes"
    )
    
    if series_number:
       query = query.eq("title", f"Series {series_number.value}")
    
    try:
        response = query.execute()
    except Exception as e:
        logger.error(f"Query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Series not found")
    
    return [
        Series(**series) for series in response.data
    ]