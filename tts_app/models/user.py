import uuid
from datetime import datetime 
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.sql import func
from tts_app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    created_at = Column(DateTime, default=func.now())
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat()
        }