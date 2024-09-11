from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/audio", tags=["audio"])

@router.get("/")
async def get_audio():
    return {"audio": "audio endpoint"}