from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/lines", tags=["line"])

@router.get("/")
async def get_lines():
    return {"line": "line endpoint"}