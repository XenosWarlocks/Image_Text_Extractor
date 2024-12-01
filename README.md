# Image_Text_Extractor

## Image and PDF Text Extractor with Filtering

This project extracts text from images and PDFs, filters it based on configurable terms, identifies names using Named Entity Recognition (NER), and stores the results in a PostgreSQL database.

## Features
- Text extraction from images and PDFs
- Fuzzy matching for text filtering
- Named Entity Recognition for accurate name detection
- Batch processing with multi-threading
- Configurable options via `config.json`
- Results saved in PostgreSQL
- Progress tracking with tqdm

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/XenosWarlocks/Image_Text_Extractor.git
   cd Image_Text_Extractor
   ```

2. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
3. Set up PostgreSQL:

    - Create a database using the config in `config.json`.

4. Update the `config.json` file with your desired settings.

## Configuration

Modify the `config.json` file to:

- Customize terms for removal.
- Enable/disable multi-threading.
- Set database connection details.

### Tests & Usage

Run unit tests:

```bash
python -m unittest discover tests
```

Run the script:
```bash
python main.py
```


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
