import unittest
from modules.filters import TextFilter

class TestTextFilter(unittest.TestCase):
    def setUp(self):
        # Mock logger
        class Logger:
            def info(self, msg): pass
            def error(self, msg): pass
        
        self.logger = Logger()
        self.remove_terms = ["test", "sample"]
        self.filter = TextFilter(self.remove_terms, self.logger)

    def test_apply_filters(self):
        text = "This is a test string with sample data."
        filtered_text = self.filter.apply_filters(text)
        self.assertNotIn("test", filtered_text)
        self.assertNotIn("sample", filtered_text)

    def test_extract_names(self):
        text = "John Doe and Alice Smith are present."
        names = self.filter.extract_names(text)
        self.assertIn("John Doe", names)
        self.assertIn("Alice Smith", names)