from fastapi import APIRouter, HTTPException

from db.supabase import SupabaseClient

router = APIRouter(prefix="/meme", tags=["meme"])

db = SupabaseClient().get_client()

@router.get("/")
async def get_memes():
    response = db.table("meme_metadata").select("*").execute()
    print(type(response))
    return response