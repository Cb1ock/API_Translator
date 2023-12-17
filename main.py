from openai import OpenAI
from pathlib import Path

from Translator import Translator
from TTS import TextToSpeech
from ASR import whisper_user
import whisper

import sys
import os

if __name__ == "__main__":

    # Target_language, load_files 
    API_KEY = "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"
    audio_path = './data/alloy.wav'
    base_name = os.path.basename(audio_path)
    file_name = os.path.splitext(base_name)[0]

    if False:
        Detected_language = "Chinese_simplified"
        Target_language = "English"
    else:
        Detected_language = "English"
        Target_language = "Chinese_simplified"

    model="whisper-1", 
    
    # ASR
    whisper_instance = whisper_user(api_key=API_KEY, model=model,audio_path=audio_path)
    # Detected_language = "Chinese"
    transcript = whisper_instance.ASR()
    print(f"transcript = {transcript.text}")
    

    # Translator
    Translator = Translator(API_KEY)
    translated_text = Translator.translate_text(transcript.text, Detected_language, Target_language)
    print(f"translated_text = {translated_text}")


    # TTS
    tts = TextToSpeech(API_KEY)
    speech_file_path = Path(__file__).parent /"results" /f"{file_name}_{Target_language}.mp3"
    tts.create_speech(translated_text, speech_file_path)