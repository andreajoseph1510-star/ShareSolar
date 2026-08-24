from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from gtts import gTTS
import tempfile
import os

router = APIRouter(prefix="/voice")

# --- Helper: Text to Speech ---
def text_to_speech(text: str, language: str = "en"):
    tts = gTTS(text=text, lang=language)
    filename = "output.mp3"
    tts.save(filename)
    return FileResponse(filename, media_type="audio/mpeg")

# --- Endpoint: Speak arbitrary text ---
@router.post("/speak")
async def speak(text: str):
    return text_to_speech(text)

# --- Endpoint: Transcribe uploaded audio ---
@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Placeholder transcription logic
    # Replace with Whisper or other speech-to-text library
    transcript = f"Received audio file: {file.filename}. (Transcription not yet implemented.)"

    # Clean up temp file
    os.remove(tmp_path)

    return {"transcript": transcript}
