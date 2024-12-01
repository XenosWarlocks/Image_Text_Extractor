import re
from rapidfuzz import fuzz, process

class TextFilter:
    def __init__(self, remove_terms, gemini_client, logger):
        self.remove_terms = remove_terms
        self.gemini_client = gemini_client
        self.logger = logger

    def apply_filters(self, text):
        for term in self.remove_terms:
            text = text.replace(term, '')
        return text

    def extract_names(self, text):
        # # Refine regex to avoid false positives
        # name_pattern = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b'
        # return re.findall(name_pattern, text)'
        # Use Google Gemini for extracting named entities
        response = self.gemini_client.analyze_text(text)
        if not response:
            self.logger.error("Failed to retrieve response from Google Gemini.")
            return []
        
        # Parse entities from the Gemini response
        entities = response.get('text', "").split("\n")
        return[entity.strip() for entity in entities if entities.strip()]
