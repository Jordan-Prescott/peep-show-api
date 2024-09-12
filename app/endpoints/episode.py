from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/episodes", tags=["episode"])

@router.get("/")
async def get_episodes():
    return {"episode": "episode endpoint"}