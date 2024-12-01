import re
from rapidfuzz import fuzz, process

class TextFilter:
    def __init__(self, remove_terms, logger):
        self.remove_terms = remove_terms
        self.logger = logger

    def apply_filters(self, text):
        for term in self.remove_terms:
            text = text.replace(term, '')
        return text

    def extract_names(self, text):
        # Refine regex to avoid false positives
        name_pattern = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b'
        return re.findall(name_pattern, text)