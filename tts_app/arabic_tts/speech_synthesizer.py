import os
import io
import base64

from gtts import gTTS


class TTS:
    def __init__(self, text):
        self.text = text
    
    def generate_audio(self):
        if not self.text:
                return None
        res = gTTS(text=self.text, lang='ar', slow=False)
        audio_data = io.BytesIO()
        res.write_to_fp(audio_data)
        audio_base64 = base64.b64encode(audio_data.getvalue()).decode('utf-8')
        
        return audio_base64
