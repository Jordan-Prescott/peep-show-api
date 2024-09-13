from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.character import Character

router = APIRouter(prefix="/characters", tags=["character"])

db = SupabaseClient().get_client()

@router.get("/", response_model=List[Character])
async def get_characters(
    first_name: Optional[str] = Query(None, example="Jeremy"),
    last_name: Optional[str] = Query(None, example="Usborne")
    ) -> List[Character]:
    
    query = db.table("character").select(
        "first_name, last_name, first_appearance, last_appearance, \
            total_episodes, actor(first_name, last_name)"
    )

    if first_name:
        first_name = first_name.capitalize()
        query = query.like("first_name", f"%{first_name}%")
    if last_name:
        last_name = last_name.capitalize()
        query = query.like("last_name", f"%{last_name}%")
        
    response = query.execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Character not found")
    
    return [
        Character(**character) for character in response.data
    ]