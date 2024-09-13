from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.location import Location

router = APIRouter(prefix="/locations", tags=["locations"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Location])
async def get_locations(
    name: Optional[str] = Query(None, example="JLB")
    ) -> List[Location]:
    
    query = db.table("location").select(
        "name"
    )
    
    if name:
        query = query.like("name", f"%{name}%")
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return [
        Location(**location) for location in response.data
    ]