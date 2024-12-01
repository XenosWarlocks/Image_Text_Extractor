import google.generativeai as genai

class GoogleGeminiClient:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
    
    def analyze_text(self, text):
        """
        Use Google Gemini API to extract information from text.
        Returns extracted insights (e.g., NER results).
        """
        try:
            response = genai.generate_text(
                prompt=f"Extract named entities (e.g., PERSON, ORGANIZATION) from the following text:\n{text}",
                model="gemini-1.5-pro"
            )
            return response
        except Exception as e:
            print(f"Error using Google Gemini API: {e}")
            return None
