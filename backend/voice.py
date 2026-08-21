from fastapi import APIRouter
from pydantic import BaseModel
import whisper
from gtts import gTTS
import io
from fastapi.responses import StreamingResponse

router = APIRouter()

class VoiceRequest(BaseModel):
    text: str
    language: str = "en"

@router.post("/speak")
def speak(request: VoiceRequest):
    # Convert text to speech
    tts = gTTS(text=request.text, lang=request.language)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return StreamingResponse(mp3_fp, media_type="audio/mpeg")
