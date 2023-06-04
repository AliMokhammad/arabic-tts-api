from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tts_app.database import get_db
from tts_app.schemas.user import SignUpDto, LogInDto
import tts_app.services.auth_service as auth_service
from tts_app.utils import response_handler


router = APIRouter()


@router.post("/sign-up")
async def signup_user(user: SignUpDto, db: Session = Depends(get_db)):
    # try:
        response = await auth_service.signup_user(user, db)
        return response 
    # except:
    #     return response_handler.error(message='Error! User sign up')



@router.post("/log-in")
async def login_user(user: LogInDto, db: Session = Depends(get_db)):
    # try:
        response = await auth_service.login_user(user, db)
        return response
    # except:
    #     return response_handler.error(message='Error! User log in')


