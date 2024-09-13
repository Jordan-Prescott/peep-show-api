from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.audio import Audio
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/audio", tags=["audio"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Audio])
@limiter.limit("5/second")
async def get_audio(
    request: Request,
    file_name: Optional[str] = Query(None, example="sperm")    
    ) -> List[Audio]:
    
    query = db.table("audio_metadata").select(
        "file_name, file_type, file_url, character(first_name, last_name)"
    )
    
    if file_name:
        query = query.eq("file_name", file_name)
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Audio not found")
    
    return [
        Audio(**audio) for audio in response.data
    ]
    
    
@router.get("/random/", response_model=Audio)
@limiter.limit("5/second")
async def get_random_audio(request: Request) -> Audio:
    
    import random
    
    query = db.table("audio_metadata").select(
        "file_name, file_type, file_url"
    )
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Audio not found")
    
    return Audio(**random.choice(response.data))