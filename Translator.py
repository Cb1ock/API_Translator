import openai

class Translator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def translate_text(self, text, source_language, target_language):
        prompt = f"Translate this from {source_language} to {target_language}: {text}"
        
        response = openai.completions.create(
            model="text-davinci-003",  # Use the appropriate model
            prompt=prompt,
            max_tokens= 3072 # Adjust as needed
        )
        
        return response.choices[0].text.strip()

# Example usage
# instance = Translator(api_key="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")
# translated_text = instance.translate_text("Hello, world!", "English", "Spanish")
# print(translated_text)
