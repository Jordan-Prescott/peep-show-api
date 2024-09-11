from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/script", tags=["script"])

@router.get("/")
async def get_scripts():
    return {"script": "script endpoint"}