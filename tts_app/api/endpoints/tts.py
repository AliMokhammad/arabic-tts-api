from fastapi import Request, APIRouter, Depends
from sqlalchemy.orm import Session

from tts_app.database import get_db
from tts_app.schemas.tts import TTSDto
import tts_app.services.tts_service as tts_service
from tts_app.utils import response_handler
from tts_app.api.auth_bearer import JWTBearer



router = APIRouter()


@router.post("/", dependencies=[Depends(JWTBearer())])
async def perform_tts(data: TTSDto, req: Request, db: Session = Depends(get_db)):
    # try:
        user = req.state.user
        ar_text = data.text
        response = await tts_service.handle_tts(user, ar_text, db)
        return response 
    # except:
    #     return response_handler.error(message='Error! Perform TTS')


@router.get("/", dependencies=[Depends(JWTBearer())])
async def get_tests(db: Session = Depends(get_db)):
    # try:
        response = await tts_service.get_tests(db)
        return response 
    # except:
    #     return response_handler.error(message='Error! Get TTS Tests')


