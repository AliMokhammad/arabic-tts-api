from pydantic import BaseModel, Field

class TTSDto(BaseModel):
    text: str = Field(title="Text is required")
