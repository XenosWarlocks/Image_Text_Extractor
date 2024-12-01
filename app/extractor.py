# extract.py
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# python -m spacy download en_core_web_sm
import pytesseract
from PIL import Image
import os
from tkinter import Tk, filedialog
import re

# Set the path to the Tesseract executable if using Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Terms to remove
remove_terms = ["show.details.v", "show.phones", "usa,.with.more"]

def extract_text_from_image(image_path):
    """Extract text from a single image file"""
    try:
        # Open the image using PIL
        image = Image.open(image_path)

        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None

def filter_content(text, remove_terms):
    """Filter out unwanted terms from the extracted text."""
    # Replace periods with spaces
    content = text.replace('.', ' ')
    
    # Remove the specified terms
    for term in remove_terms:
        content = content.replace(term, '')
    
    return content

def extract_names(text):
    """Extract lines that look like names (Starting with a capital letter)."""
    # Regex pattern to identify potential names (Starting with a capital letter)
    name_pattern = r'^[A-Z][a-zA-Z\s]+'
    
    # Split the text into lines
    lines = text.split('\n')
    
    # Extract lines that match the regex
    names = [line.strip() for line in lines if re.match(name_pattern, line.strip())]
    
    return names

def batch_process_folder(folder_path):
    """Process all image files in the folder one by one."""
    results = {}
    
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check if file is an image
            print(f"Processing image: {file_path}")
            text = extract_text_from_image(file_path)

            # Filter the extracted text
            if text:
                filtered_text = filter_content(text, remove_terms)
                # Extract names from the filtered text
                names = extract_names(filtered_text)
                results[file_name] = names
            else:
                results[file_name] = None
    
    return results

def write_results_to_file(folder_path, results):
    """Write the extracted names and folder names to a text file."""
    output_file = os.path.join(folder_path, "extracted_names.txt")
    
    with open(output_file, 'w') as f:
        f.write(f"Folder: {os.path.basename(folder_path)}\n\n")
        for image_name, names in results.items():
            f.write(f"Image: {image_name}\n")
            if names:
                f.write("Names:\n")
                for name in names:
                    # Format names as firstname.lastname
                    formatted_name = name.replace(' ', '.').lower()
                    f.write(f"{formatted_name}\n")
            else:
                f.write("No names found.\n")
            f.write("\n")
    
    print(f"Results written to {output_file}")

def select_folder_and_process():
    """Open a dialog for selecting a folder with images and process them."""
    # Hide the root window
    root = Tk()
    root.withdraw()

    # Prompt the user to select a folder
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")

    if folder_path:
        results = batch_process_folder(folder_path)
        write_results_to_file(folder_path, results)
    else:
        print("No folder selected.")

# Example usage
if __name__ == "__main__":
    select_folder_and_process()


# python extractor.py removetxt.py
