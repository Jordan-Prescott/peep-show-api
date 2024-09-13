from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from .dependancies.rate_limiter import limiter
from .db.supabase import SupabaseClient
from .endpoints import all_routers

app = FastAPI()

# app setup
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
supabase_client = SupabaseClient().get_client()

for router in all_routers:
    app.include_router(router, prefix="/api")
    
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})