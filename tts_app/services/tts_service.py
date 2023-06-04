from sqlalchemy.orm import Session, joinedload

from tts_app.database import get_db
from tts_app.models.tts_test import TTSTest
from tts_app.schemas.user import SignUpDto, LogInDto

from tts_app.utils.authentication import *
from tts_app.utils import response_handler

from tts_app.arabic_tts.diacritizer import Diacritizer
from tts_app.arabic_tts.speech_synthesizer import TTS

async def handle_tts(user: SignUpDto,ar_text: str, db: Session): 
    diacritizer = Diacritizer(text=ar_text)
    diac_text = diacritizer.add_diacritics() 

    speech_synthesizer = TTS(text=diac_text)
    audio_base64 = speech_synthesizer.generate_audio()

    new_tts_test = TTSTest(
        text=ar_text, 
        diac_text=diac_text, 
        audio_base64=audio_base64, 
        user_id=user.get('user_id')
    )

    db.add(new_tts_test)
    db.commit()
    db.close()

    data = {
        'text': ar_text,
        'diac_text': diac_text,
        'audio_base64': audio_base64,
    }

    return response_handler.success(data=data)


async def get_tests(db: Session):
    tsets = db.query(TTSTest).options(joinedload(TTSTest.user)).all()
    tsets_list = []
    for test in tsets:
        tsets_list.append(test.to_dict())

    data = {"tsets": tsets_list}

    return response_handler.success(data=data)

