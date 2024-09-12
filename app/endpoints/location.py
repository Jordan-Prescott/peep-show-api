from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/locations", tags=["location"])

@router.get("/")
async def get_locations():
    return {"location": "location endpoint"}