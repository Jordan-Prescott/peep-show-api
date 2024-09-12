from fastapi import APIRouter, HTTPException

from ..db.supabase import SupabaseClient
from ..schemas.series import Series, SeriesURLChoices

router = APIRouter(prefix="/series", tags=["series"])

db = SupabaseClient().get_client()

@router.get("/")
async def get_memes(series_title: SeriesURLChoices | None = None) -> list[Series]:
    
    if series_title:
        response = db.table("series").select(
            "title, description, network, premiere_date, finale_date, number_of_episodes"
            ).eq("title", series_title).execute().dict()
        if not response:
            raise HTTPException(status_code=404, detail="Series not found")
        return [
            Series(**series) for series in response["data"]
        ]
    
    response = db.table("series").select(
        "title, description, network, premiere_date, finale_date, number_of_episodes"
        ).execute().dict()
    return [
        Series(**series) for series in response["data"]
    ]