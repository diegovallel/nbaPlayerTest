from fastapi import APIRouter

from api.api_v1.endpoints import nbaPlayers

api_router = APIRouter()
api_router.include_router(nbaPlayers.router, prefix="/nbaPlayers", tags=["users"])

