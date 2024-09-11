from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/actor", tags=["actor"])

@router.get("/")
async def get_actors():
    return {"actor": "actor endpoint"}