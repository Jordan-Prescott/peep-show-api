from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/location", tags=["location"])

@router.get("/")
async def get_locations():
    return {"location": "location endpoint"}