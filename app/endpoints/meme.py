from fastapi import APIRouter, HTTPException
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.meme import Meme

router = APIRouter(prefix="/memes", tags=["meme"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Meme])
async def get_memes(
    file_name: Optional[str] = None
    ) -> List[Meme]:
    
    query = db.table("meme_metadata").select(
        "file_name, file_type, file_url"
    )
    
    if file_name:
        query = query.eq("file_name", file_name)
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Meme not found")
    
    return [
        Meme(**meme) for meme in response.data
    ]