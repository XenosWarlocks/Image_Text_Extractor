# Image_Text_Extractor
A Python-based tool for batch processing and extracting text from images using OCR (Tesseract). The extracted text is cleaned by removing unwanted terms, and potential names are identified and formatted. Results are saved in a structured text file for easy reference. Ideal for automating data extraction and preprocessing tasks.


## Project Structure

```
ImageTextExtractor/
├── config.json           # Configuration file
├── main.py               # Entry point
├── modules/
│   ├── extractor.py      # OCR and file processing logic
│   ├── filters.py        # Text filtering and name extraction
│   ├── utils.py          # Utilities for logging and progress tracking
│   ├── db_handler.py     # Database interaction
│   ├── ner_model.py      # NER-based name extraction
├── tests/
│   ├── test_extractor.py # Unit tests for extractor
│   ├── test_filters.py   # Unit tests for filtering
│   ├── test_db.py        # Unit tests for database
├── requirements.txt      # Python dependencies
├── README.md             # Documentation

```
