import logging

from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.avatar import Avatar
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/avatars", tags=["avatars"])
db = SupabaseClient().get_client()
logger = logging.getLogger("app")

@router.get("/", response_model=List[Avatar])
@limiter.limit("5/second")
async def get_avatars(
    request: Request,
    file_name: Optional[str] = Query(None, example="Andy")
    ) -> List[Avatar]:
    
    query = db.table("avatar_metadata").select(
        "file_name, file_type, file_url"
    )
    
    if file_name:
        query = query.eq("file_name", file_name)
        logger.info(f"Searching for avatar with file name: {file_name}")
        
    try:
        response = query.execute()
    except Exception as e:
        logger.error(f"Query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Avatar not found")
    
    return [
        Avatar(**audio) for audio in response.data
    ]
    
    
@router.get("/random/", response_model=Avatar)
@limiter.limit("5/second")
async def get_random_avatar(
    request: Request
    ) -> Avatar:
    
    import random
    
    query = db.table("avatar_metadata").select(
        "file_name, file_type, file_url"
    )
    logger.info(f"Searching for random avatar")
    
    try: 
        response = query.execute()
    except Exception as e:
        logger.error(f"Query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Avatar not found")
    
    return Avatar(**random.choice(response.data))