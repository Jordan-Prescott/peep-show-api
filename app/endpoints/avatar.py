from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.avatar import Avatar

router = APIRouter(prefix="/avatars", tags=["avatars"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Avatar])
async def get_avatars(
    file_name: Optional[str] = Query(None, example="sperm"),
    first_name: Optional[str] = Query(None, example="Mark"),
    last_name: Optional[str] = Query(None, example="Corrigan")
    ) -> List[Avatar]:
    
    query = db.table("avatar_metadata").select(
        "file_name, file_type, file_url, character(first_name, last_name)"
    )
    
    if file_name:
        query = query.eq("file_name", file_name)
    if first_name:
        first_name = first_name.capitalize()
        query = query.ilike("character.first_name", f"%{first_name}%")
    if last_name:
        last_name = last_name.capitalize()
        query = query.ilike("character.last_name", f"%{last_name}%")
        
    response = query.execute()
    
    print(response.data)
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Audio not found")
    
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
        raise HTTPException(status_code=404, detail="Audio not found")
    
    return Avatar(**random.choice(response.data))