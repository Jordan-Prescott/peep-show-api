import logging

from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional

from ..db.supabase import SupabaseClient
from ..schemas.line import Line, LineFilter
from ..dependancies.rate_limiter import limiter

router = APIRouter(prefix="/quotes", tags=["quotes"])
db = SupabaseClient().get_client()
logger = logging.getLogger("app")

@router.get("/search/", response_model=List[Line])
@limiter.limit("5/second")
async def get_quotes(
    request: Request,
    quote: str = Query(..., min_length=8, example="everything's cool in Dobby Club.")
    ) -> List[Line]:
    
    sanitised_quote = quote.strip()
    logger.info(f"Searching for quote: {sanitised_quote}")
    
    query = db.table("line").select(
        "line_content, spoken_by, spoken_to, line_number, \
            script(series, episode), location(name), meme_metadata(file_name, file_type, file_url)"
    ).limit(100)
    
    query = query.ilike("line_content", f"%{sanitised_quote}%")
    
    try:
        response = query.execute()
        logging.info(f"Response: {response}")
    except Exception as e: 
        logging.error(f"Query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

    if not response.data:
        raise HTTPException(status_code=404, detail="Quote not found")
    
    return [
        Line(**line) for line in response.data
    ]
    
    
@router.get("/filter/", response_model=List[LineFilter])
@limiter.limit("5/second")
async def get_quotes_filter(
    request: Request,
    spoken_by: Optional[str] = Query(None, example="Mark"),
    spoken_to: Optional[str] = Query(None, example="Jeremy"),
    ) -> List[LineFilter]:

    query = db.table("line").select(
        "line_content, spoken_by, spoken_to, line_number"
        )
    
    if spoken_by:
        spoken_by = spoken_by.capitalize()
        query = query.ilike("spoken_by", spoken_by)
        logger.info(f"Searching for quotes spoken by: {spoken_by}")
    if spoken_to:
        spoken_to = spoken_to.capitalize()
        query = query.ilike("spoken_to", spoken_to)
        logger.info(f"Searching for quotes spoken to: {spoken_to}")
    
    try:   
        response = query.execute()
    except Exception as e:
        logger.error(f"Query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Quote not found")
    
    return [
        LineFilter(**line) for line in response.data
    ]
    

@router.get("/random/", response_model=LineFilter)
@limiter.limit("5/second")
async def get_random_quotes(
    request: Request
    ) -> LineFilter:

    import random

    query = db.table("line").select(
        "line_content, spoken_by, spoken_to, line_number"
        )
    
    try:  
        response = query.execute()
    except Exception as e:
        logger.error(f"Query failed with error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Quote not found")

    return LineFilter(**random.choice(response.data))
    
    