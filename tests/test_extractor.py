import unittest
from modules.extractor import OCRExtractor

class TestOCRExtractor(unittest.TestCase):
    def setup(self):
        # Mock logger
        class logger:
            def info(self, msg): pass
            def error(self, msg): pass
        
        self.logger = logger()
        self.extractor = OCRExtractor(self.logger)
    
    def test_extract_text_from_image(self):
        sample_image = "sample/sample_image.png" # # Place a sample image in the sample folder
        text = self.extractor.extract_text_from_image(sample_image)
        self.assertIsNotNone(text)
        self.assertTrue(len(text) > 0)
    
    def test_extract_text_from_pdf(self):
        sample_pdf = "sample/sample.pdf"  # Place a sample PDF in the sample folder
        text = self.extractor.extract_text_from_pdf(sample_pdf)
        self.assertIsNotNone(text)
        self.assertTrue(len(text) > 0)