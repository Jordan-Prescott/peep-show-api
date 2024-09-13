from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.aduio import Audio

router = APIRouter(prefix="/audio", tags=["audio"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Audio])
async def get_memes(
    file_name: Optional[str] = Query(None, 
                                     example="sperm"
                                    )    
    ) -> List[Audio]:
    
    query = db.table("audio_metadata").select(
        "file_name, file_type, file_url"
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
async def get_memes() -> Audio:
    
    import random
    
    query = db.table("audio_metadata").select(
        "file_name, file_type, file_url"
    )
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Audio not found")
    
    return Audio(**random.choice(response.data))