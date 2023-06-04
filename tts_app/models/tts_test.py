import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from tts_app.database import Base
from tts_app.models.user import User

class TTSTest(Base):
    __tablename__ = "tts_tests"
    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String)
    diac_text = Column(String)
    audio_base64 = Column(String)
    user_id = Column(String, ForeignKey("users.id"))
    user = relationship(User)
    created_at = Column(DateTime, default=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "diac_text": self.diac_text,
            "audio_base64": self.audio_base64,
            "user_id": self.user_id,
            "user": self.user.to_dict() if self.user else None,
            "created_at": self.created_at.isoformat()
        }