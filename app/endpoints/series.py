from fastapi import APIRouter, HTTPException

from ..db.supabase import SupabaseClient
from ..schemas.series import Series, SeriesURLChoices

router = APIRouter(prefix="/series", tags=["series"])

db = SupabaseClient().get_client()

@router.get("/")
async def get_series(series_num: SeriesURLChoices | None = None) -> list[Series]:
    
    if series_num:
        response = db.table("series").select(
            "title, description, network, premier_date, finale_date, number_of_episodes"
            ).eq("title", f"Series {series_num.value}").execute().dict()
        if not response:
            raise HTTPException(status_code=404, detail="Series not found")
        return [
            Series(**series) for series in response["data"]
        ]
    
    response = db.table("series").select(
        "title, description, network, premier_date, finale_date, number_of_episodes"
        ).execute().dict()
    return [
        Series(**series) for series in response["data"]
    ]