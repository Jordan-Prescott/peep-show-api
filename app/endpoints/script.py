from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/scripts", tags=["script"])

@router.get("/")
async def get_scripts():
    return {"script": "script endpoint"}