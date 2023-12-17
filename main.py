from openai import OpenAI
from pathlib import Path

from Translator import Translator
from TTS import TextToSpeech
from ASR import whisper_user
import whisper

import sys
import os

if __name__ == "__main__":

    # 检查命令行参数数量
    if len(sys.argv) < 3:
        print("Usage: python main.py <target_language> <audio_file_path>")
        sys.exit(1)

    # 获取命令行参数
    Target_language = sys.argv[1]
    audio_path = sys.argv[2]

    API_KEY = "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"
    base_name = os.path.basename(audio_path)
    file_name = os.path.splitext(base_name)[0]

    # 假设您已经有了检测语言的逻辑
    # 在这里您可以根据需要调整 Detected_language 的获取方式
    Detected_language = "English"  # 或者使用您的逻辑来确定

    model = "whisper-1"
    
    # ASR
    whisper_instance = whisper_user(api_key=API_KEY, model=model, audio_path=audio_path)
    transcript = whisper_instance.ASR()
    print(f"transcript = {transcript.text}")
    

    # Translator
    translator_instance = Translator(API_KEY)
    translated_text = translator_instance.translate_text(transcript.text, Detected_language, Target_language)
    print(f"translated_text = {translated_text}")

    # TTS
    tts = TextToSpeech(API_KEY)
    speech_file_path = Path(__file__).parent / "results" / f"{file_name}_{Target_language}.mp3"
    tts.create_speech(translated_text, speech_file_path)
