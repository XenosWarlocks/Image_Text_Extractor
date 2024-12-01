import re
from rapidfuzz import fuzz, process
import google.generativeai as genai


class TextFilter:
    def __init__(self, remove_terms, gemini_client, logger):
        self.remove_terms = remove_terms
        self.gemini_client = gemini_client
        self.logger = logger

    def apply_filters(self, text):
        # First, extract names
        names = self.extract_names(text)

        # Log extracted names
        if names:
            self.logger.info(f"Extracted names: {names}")
            return names
        
        return []

    def extract_names(self, text):
        # Use Google Gemini for extracting named entities
        try:
            # Use Gemini first
            gemini_entities = self.gemini_client.analyze_text(text)
            if gemini_entities:
                return gemini_entities
            
            # Fallback to regex for name extraction
            name_pattern = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b'
            regex_names = re.findall(name_pattern, text)

            # Filter out common non-name words
            filtered_names = [
                name for name in regex_names if name not in ['Wharton', 'Online', 'Customer', 'Analytics', 'Prepaid']
            ]
            return filtered_names
            
        except Exception as e:
            self.logger.error(f"Name extraction error: {e}")
            return []

    def _get_gemini_names(self, text):
        try:
            model = genai.GenerativeModel('gemini-pro')
            prompt = (
                "From the following text, extract ONLY proper names of people. "
                "Return a comma-separated list of names. If no names are found, return an empty list.\n\n"
                f"{text}"
            )
            response = model.generate_content(prompt)

            # Parse names from response
            if response and response.text:
                # Split and clean names
                names = [name.strip() for name in response.text.split(',') if name.strip()]
                return names
            
            return []
        except Exception as e:
            self.logger.error(f"Gemini name extraction error: {e}")
            return []
