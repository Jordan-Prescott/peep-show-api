from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/avatar", tags=["avatar"])

@router.get("/")
async def get_avatars():
    return {"avatar": "avatar endpoint"}