from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/line", tags=["line"])

@router.get("/")
async def get_lines():
    return {"line": "line endpoint"}