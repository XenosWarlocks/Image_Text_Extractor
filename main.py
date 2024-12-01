# main.py
import json
from modules.extractor import OCRExtractor
from modules.filters import TextFilter
from modules.utils import setup_logging, ProgressTracker
from modules.db_handler import DBHandler

def main():
    # Load configuration
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    
    # Set up logging
    logger = setup_logging("text_extractor.log")
    logger.info("Application started")
    
    # Initialize classes
    db_handler = DBHandler(config["db_config"])
    ocr_extractor = OCRExtractor(logger)
    text_filter = TextFilter(config["remove_terms"], logger)

    # Select folder and process
    folder_path = ocr_extractor.select_folder()
    if folder_path:
        results = ocr_extractor.batch_process_folder(folder_path, text_filter)
        db_handler.save_results(results)
        logger.info("Processing completed")
    else:
        logger.info("No folder selected. Exiting...")

if __name__ == "__main__":
    main()
