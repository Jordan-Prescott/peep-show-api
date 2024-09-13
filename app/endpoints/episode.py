from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/episodes", tags=["episode"])

@router.get("/")
async def get_episodes():
    return {"episode": "episode endpoint"}


# @router.get("/episodes/", response_model=List[Episode])
# async def get_characters(
#     first_name: Optional[str] = None,
#     last_name: Optional[str] = None
#     ) -> List[Episode]:
    
#     query = db.table("character_episode").select(
#         "episode(title, overall_episode_number, episode_number, air_date, \
#             directors, writers, synopsis), character(first_name, last_name)"
#     )

#     if first_name:
#         first_name = first_name.capitalize()
#         query = query.like("character.first_name", f"%{first_name}%")
#     if last_name:
#         last_name = last_name.capitalize()
#         query = query.like("character.last_name", f"%{last_name}%")
        
#     response = query.execute()
    
#     print(response.data)
    
#     if not response.data:
#         raise HTTPException(status_code=404, detail="Episodes not found")
    
#     return [
#         Episode(**episode["episode"]) for episode in response.data if episode["character"] is not None
#     ]