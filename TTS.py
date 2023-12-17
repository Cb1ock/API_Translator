from openai import OpenAI
import os

class TextToSpeech:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def create_speech(self, text, output_file):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text,
        )
        response.stream_to_file(output_file)
            

# # test
# tts_instance = TextToSpeech(api_key="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")
# tts_instance.create_speech("In this paper, we first extend the recent Masked Auto-Encoder (MAE) model from a single modality to audio-visual multi-modalities. Subsequently, we propose the Contrastive Audio-Visual Masked Auto-Encoder (CAV-MAE) by combining contrastive learning and masked data modeling, two major self-supervised learning frameworks, to learn a joint and coordinated audio-visual representation. Our experiments show that the contrastive audio-visual correspondence learning objective not only enables the model to perform audio-visual retrieval tasks, but also helps the model learn a better joint representation. As a result, our fully self-supervised pretrained CAV-MAE achieves a new SOTA accuracy of 65.9% on VGGSound, and is comparable with the previous best supervised pretrained model on AudioSet in the audio-visual event classification task.", "speech.mp3")