import whisper
from openai import OpenAI
class whisper_user:
    def __init__(self,api_key,model,audio_path):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.audio = audio_path
    
    def ASR(self):
        audio_file= open(self.audio, "rb")
        transcript = self.client.audio.transcriptions.create(
          model="whisper-1", 
          file=audio_file
        )
        return transcript


'''import whisper

class whisper_user:
    def __init__(self, audio):
        self.model = whisper.load_model("base")

        # load audio and pad/trim it to fit 30 seconds
        self.audio = audio
        audio = whisper.pad_or_trim(audio)

        # make log-Mel spectrogram and move to the same device as the model
        self.mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

    def detect_language(self):
        _, probs = self.model.detect_language(self.mel)
        print(f"Detected language: {max(probs, key=probs.get)}")
        Detected_language = max(probs, key=probs.get)
        return Detected_language

    def ASR(self):
        # decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, self.mel, options)
        return result.text


# import whisper
# model = whisper.load_model("base")
# result = model.transcribe("audio.mp3")
# print(result["text"])'''