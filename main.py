# main.py
import json
from modules.extractor import OCRExtractor
from modules.filters import TextFilter
from modules.utils import setup_logging, ProgressTracker
from modules.db_handler import DBHandler
from modules.geminiai import GoogleGeminiClient

def main():
    # Load configuration
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    
    # Set up logging
    logger = setup_logging("text_extractor.log")
    logger.info("Application started")

    # Initialize Google Gemini client
    gemini_client = GoogleGeminiClient(api_key=config["google_gemini_api_key"])
    
    # Initialize classes
    # db_handler = DBHandler(config["db_config"])
    ocr_extractor = OCRExtractor(logger)
    text_filter = TextFilter(config["remove_terms"], gemini_client, logger)

    # Select folder and process
    folder_path = ocr_extractor.select_folder()
    if folder_path:
        results = ocr_extractor.batch_process_folder(folder_path, text_filter)
        # db_handler.save_results(results)
        # Interactive processing of results
        for filename, extracted_names in results.items():
            print(f"File: {filename}")
            if extracted_names:
                print("Extracted Names:")
                for name in extracted_names:
                    print(f"- {name}")

                # Optional: Ask if user wants to do something with the names
                action = input("Would you like to perform any action with these names? (y/n): ").lower()
                if action == 'y':
                    further_action = input("What would you like to do? (1: Gemini Analysis, 2: Save, 3: Other): ")
                    if further_action == '1':
                        # Example of using Gemini for additional analysis
                        for name in extracted_names:
                            analysis = gemini_client.additional_name_analysis(name)
                            print(f"Analysis for {name}: {analysis}")

            else:
                print("No names extracted.")

        logger.info("Processing completed")
    else:
        logger.info("No folder selected. Exiting...")

if __name__ == "__main__":
    main()
