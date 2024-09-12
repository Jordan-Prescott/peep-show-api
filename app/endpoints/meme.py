from fastapi import APIRouter, HTTPException

from db.supabase import SupabaseClient
from schemas import Meme

router = APIRouter(prefix="/memes", tags=["meme"])

db = SupabaseClient().get_client()

@router.get("/")
async def get_memes(file_name: str = None) -> list[Meme]:
    
    if file_name:
        response = db.table("meme_metadata").select("file_name, file_type, file_url").eq("file_name", file_name).execute().dict()
        if not response:
            raise HTTPException(status_code=404, detail="Meme not found")
        return [
            Meme(**meme) for meme in response["data"]
        ]
    
    response = db.table("meme_metadata").select("file_name, file_type, file_url").execute().dict()
    return [
        Meme(**meme) for meme in response["data"]
    ]