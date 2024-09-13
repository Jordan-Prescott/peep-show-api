from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.avatar import Avatar

router = APIRouter(prefix="/avatars", tags=["avatars"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Avatar])
async def get_avatars(
    file_name: Optional[str] = Query(None, example="sperm")
    ) -> List[Avatar]:
    
    query = db.table("avatar_metadata").select(
        "file_name, file_type, file_url"
    )
    
    if file_name:
        query = query.eq("file_name", file_name)
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Avatar not found")
    
    return [
        Avatar(**audio) for audio in response.data
    ]
    
    
@router.get("/random/", response_model=Avatar)
async def get_random_avatar() -> Avatar:
    
    import random
    
    query = db.table("avatar_metadata").select(
        "file_name, file_type, file_url"
    )
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Avatar not found")
    
    return Avatar(**random.choice(response.data))