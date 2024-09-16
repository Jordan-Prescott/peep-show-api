from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.location import Location
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/locations", tags=["locations"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Location])
@limiter.limit("5/second")
async def get_locations(
    request: Request,
    name: Optional[str] = Query(None, example="JLB")
    ) -> List[Location]:
    
    query = db.table("location").select(
        "name"
    )
    
    if name:
        name = name.strip()
        query = query.ilike("name", f"%{name}%")
    
    try:    
        response = query.execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail="test error message")
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return [
        Location(**location) for location in response.data
    ]