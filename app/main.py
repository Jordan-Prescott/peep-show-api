from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db.supabase import SupabaseClient
from app.endpoints import all_routers

app = FastAPI()

# app setup
supabase_client = SupabaseClient().get_client()

for router in all_routers:
    app.include_router(router, prefix="/api")
    
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})