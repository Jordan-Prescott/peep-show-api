import logging

from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.character import Character
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/characters", tags=["character"])
db = SupabaseClient().get_client()
logger = logging.getLogger("app")

@router.get("/", response_model=List[Character])
@limiter.limit("5/second")
async def get_characters(
    request: Request,
    first_name: Optional[str] = Query(None, example="Jeremy"),
    last_name: Optional[str] = Query(None, example="Usborne")
    ) -> List[Character]:
    
    query = db.table("character").select(
        "first_name, last_name, first_appearance, last_appearance, \
            total_episodes, actor(first_name, last_name)"
    )

    if first_name:
        first_name = first_name.capitalize()
        query = query.ilike("first_name", f"%{first_name}%")
        logger.info(f"Searching for character with first name: {first_name}")
    if last_name:
        last_name = last_name.capitalize()
        query = query.ilike("last_name", f"%{last_name}%")
        logger.info(f"Searching for character with last name: {last_name}")
    
    try:
        response = query.execute()
    except Exception as e:
        logger.error(f"Query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")    
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Character not found")
    
    return [
        Character(**character) for character in response.data
    ]