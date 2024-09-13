from fastapi import APIRouter, HTTPException, Request
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.series import Series, SeriesURLChoices
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/series", tags=["series"])

db = SupabaseClient().get_client()

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
    
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Series not found")
    
    return [
        Series(**series) for series in response.data
    ]