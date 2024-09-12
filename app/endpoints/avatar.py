from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/avatars", tags=["avatar"])

@router.get("/")
async def get_avatars():
    return {"avatar": "avatar endpoint"}