from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.actor import Actor
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/actors", tags=["actors"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Actor])
@limiter.limit("5/second")
async def get_actors(
    request: Request,
    first_name: Optional[str] = Query(None, example="Robert"),
    last_name: Optional[str] = Query(None, example="Webb")
    ) -> List[Actor]:
    
    query = db.table("actor").select(
        "first_name, last_name, gender, participation_range, total_episodes"
    )

    if first_name:
        first_name = first_name.capitalize()
        query = query.eq("first_name", first_name)
    if last_name:
        last_name = last_name.capitalize()
        query = query.eq("last_name", last_name)

    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Actors not found")

    return [
        Actor(**actor) for actor in response.data
    ]
