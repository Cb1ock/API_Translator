from openai import OpenAI
client = OpenAI(api_key="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")

audio_file= open("alloy.wav", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcript)