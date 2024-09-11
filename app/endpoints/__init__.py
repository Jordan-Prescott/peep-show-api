from .actor import router as actor_router
from .audio import router as audio_router
from .avatar import router as avatar_router
from .character import router as character_router
from .episode import router as episode_router
from .line import router as line_router
from .location import router as location_router
from .meme import router as meme_router
from .script import router as script_router

# loaded in app/main.py
all_routers = [
    actor_router,
    audio_router,
    avatar_router,
    character_router,
    episode_router,
    line_router,
    location_router,
    meme_router,
    script_router,
]