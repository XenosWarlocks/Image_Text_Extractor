import os
import pytesseract
from PIL import Image
from tqdm import tqdm
import pdfplumber
import concurrent.futures
from tkinter import Tk, filedialog
from modules.filters import TextFilter

class OCRExtractor:
    def __init__(self, logger):
        self.logger = logger
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def select_folder(self):
        root = Tk()
        root.withdraw()
        return filedialog.askdirectory(title="Select Folder Containing Images")
    
    def extract_text_from_image(self, image_path):
        try:
            image = Image.open(image_path)
            return pytesseract.image_to_string(image)
        except Exception as e:
            self.logger.error(f"Error extracting text from image {image_path}: {e}")
            return None
        
    def extract_text_from_pdf(self, pdf_path):
        try:
            text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            return text
        except Exception as e:
            self.logger.error(f"Error extracting text from PDF {pdf_path}: {e}")
            return None

    def batch_process_folder(self, folder_path, text_filter):
        results = {}
        file_list = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf'))]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {}
            for file_name in file_list:
                file_path = os.path.join(folder_path, file_name)
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    futures[executor.submit(self.extract_text_from_image, file_path)] = file_name
                elif file_name.lower().endswith('.pdf'):
                    futures[executor.submit(self.extract_text_from_pdf, file_path)] = file_name
                
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Files"):
                file_name = futures[future]
                text = future.result()
                if text:
                    results[file_name] = text_filter.apply_filters(text)
                else:
                    results[file_name] = None
        
        return results