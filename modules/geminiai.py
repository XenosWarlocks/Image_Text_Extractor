import time
import google.generativeai as genai

class GoogleGeminiClient:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.rate_limit_wait = 60  # seconds to wait if rate limited
    
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
        """Perform additional analysis on a extracted name with rate limit handling"""
        try:
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Provide a brief professional context or background for the name: {name}"

            # Add retry mechanism for rate limiting
            for attempt in range(3):
                try:
                    response = model.generate_content(prompt)
                    return response.text.strip() if response and response.text else "No additional information found."
                
                except Exception as e:
                    if '429' in str(e):
                        print(f"Rate limit reached. Waiting {self.rate_limit_wait} seconds...")
                        time.sleep(self.rate_limit_wait)
                    else:
                        raise
            
            return "Analysis failed after multiple attempts."
        
        except Exception as e:
            print(f"Error in name analysis: {e}")
            return "Analysis failed."
