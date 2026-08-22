from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from gtts import gTTS
import whisper
import os

router = APIRouter()

# --- Ensure ffmpeg is visible to Whisper ---
# Adjust this path if your ffmpeg.exe is installed elsewhere
os.environ["PATH"] += os.pathsep + r"C:\Program Files\ffmpeg\bin"

# --- Load Whisper model once at startup ---
# Explicitly set device to CPU to avoid FP16 warnings
model = whisper.load_model("small", device="cpu")

# --- Text to Speech ---
@router.post("/voice/speak")
async def speak_text(text: str, language: str = "en"):
    """Convert text into speech and return an MP3 file."""
    tts = gTTS(text=text, lang=language)
    filename = "output.mp3"
    tts.save(filename)
    return FileResponse(filename, media_type="audio/mpeg")

# --- Speech to Text ---
@router.post("/voice/transcribe")
async def transcribe(file: UploadFile = File(...)):
    """Transcribe uploaded audio into text using Whisper."""
    audio_path = f"temp_{file.filename}"
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    result = model.transcribe(audio_path)

    # Clean up temp file
    if os.path.exists(audio_path):
        os.remove(audio_path)

    return {"transcript": result["text"]}
