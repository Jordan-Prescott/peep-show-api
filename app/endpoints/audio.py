from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/audios", tags=["audio"])

@router.get("/")
async def get_audio():
    return {"audio": "audio endpoint"}