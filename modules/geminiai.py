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
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Extract named entities (PERSON, ORGANIZATION) from this text. Return as a list:\n{text}"
            response = model.generate_content(prompt)

            # Check if response is valid
            if response and response.text:
                # Parse entities from the response
                return [entity.strip() for entity in response.text.split('\n') if entity.strip()]
            return []
        except Exception as e:
            print(f"Error using Google Gemini API: {e}")
            return None
        
    def additional_name_analysis(self, name):
        """Perform additional analysis on a extracted name"""
        try:
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Provide a brief professional context or background for the name: {name}"
            response = model.generate_content(prompt)
            
            return response.text.strip() if response and response.text else "No additional information found."
        
        except Exception as e:
            print(f"Error in name analysis: {e}")
            return "Analysis failed."
