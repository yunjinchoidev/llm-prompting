# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
from load_dotenv import load_dotenv

load_dotenv()
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
audio_file = open("./whisper/audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
text_eng = transcript["text"]
print(text_eng)
# print(transcript)

# 저장
with open("./whisper/transcript.txt", "w") as f:
    f.write(text_eng)
