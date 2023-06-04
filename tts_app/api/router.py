from fastapi import APIRouter

from .endpoints import auth_router, tts_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(tts_router, prefix="/tts", tags=["tts"])
