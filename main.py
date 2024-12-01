# main.py
import json
import os
import csv
from modules.extractor import OCRExtractor
from modules.filters import TextFilter
from modules.utils import setup_logging, ProgressTracker
from modules.db_handler import DBHandler
from modules.geminiai import GoogleGeminiClient

def create_data_folder(base_path='data'):
    """
    Create a data folder if it doesn't exist.
    Returns the full path to the created folder.
    """
    data_path = os.path.abspath(base_path)
    os.makedirs(data_path, exist_ok=True)
    return data_path

def save_results_to_files(results, data_folder):
    """
    Save extracted names to CSV and TXT files.
    
    Args:
        results (dict): Dictionary of filename to extracted names
        data_folder (str): Path to the data folder
    """
    # Prepare timestamp for unique filenames
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # CSV file
    csv_path = os.path.join(data_folder, f'extracted_names_{timestamp}.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Source File', 'Extracted Names'])
        
        for filename, names in results.items():
            if names:
                for name in names:
                    csv_writer.writerow([filename, name])
    
    # TXT file
    txt_path = os.path.join(data_folder, f'extracted_names_{timestamp}.txt')
    with open(txt_path, 'w', encoding='utf-8') as txtfile:
        for filename, names in results.items():
            txtfile.write(f"Source File: {filename}\n")
            if names:
                for name in names:
                    txtfile.write(f"- {name}\n")
            else:
                txtfile.write("No names extracted\n")
            txtfile.write("\n")
    
    print(f"Results saved to:")
    print(f"- CSV: {csv_path}")
    print(f"- TXT: {txt_path}")

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
    
    # Initialize classes
    ocr_extractor = OCRExtractor(logger)
    text_filter = TextFilter(config["remove_terms"], gemini_client, logger)

    # Select folder and process
    folder_path = ocr_extractor.select_folder()
    if folder_path:
        results = ocr_extractor.batch_process_folder(folder_path, text_filter)
        # db_handler.save_results(results)
        
        # Interactive processing of results
        final_results = {}
        for filename, extracted_names in results.items():
            print(f"\nFile: {filename}")
            if extracted_names:
                print("Extracted Names:")
                for name in extracted_names:
                    print(f"- {name}")
                
                # Store names for potential later use
                final_results[filename] = extracted_names
                
                # Ask for action
                while True:
                    action = input(
                        "Actions:\n"
                        "1: Gemini Analysis\n"
                        "2: Skip this file\n"
                        "3: Save All Results\n"
                        "4: Exit Program\n"
                        "Enter your choice (1-4): "
                    )
                    
                    if action == '1':
                        # Gemini Analysis
                        for name in extracted_names:
                            try:
                                analysis = gemini_client.additional_name_analysis(name)
                                print(f"Analysis for {name}: {analysis}")
                            except Exception as e:
                                print(f"Analysis failed for {name}: {e}")
                    
                    elif action == '2':
                        # Skip to next file
                        break
                    
                    elif action == '3':
                        # Save all results to data folder
                        data_folder = create_data_folder()
                        save_results_to_files(final_results, data_folder)
                    
                    elif action == '4':
                        # Exit the entire program
                        print("Exiting program.")
                        logger.info("Program exited by user")
                        return
                    
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("No names extracted.")
        
        # Final option to save at the end
        save_choice = input("Do you want to save all extracted names? (y/n): ").lower()
        if save_choice == 'y':
            data_folder = create_data_folder()
            save_results_to_files(final_results, data_folder)
        
        logger.info("Processing completed")
    else:
        logger.info("No folder selected. Exiting...")

if __name__ == "__main__":
    main()
