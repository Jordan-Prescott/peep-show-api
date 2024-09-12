from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/characters", tags=["character"])

@router.get("/")
async def get_characters():
    return {"character": "character endpoint"}