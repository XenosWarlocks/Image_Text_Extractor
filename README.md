# Image_Text_Extractor

# Image and PDF Text Extractor with Filtering

This Python-based Text Extraction and Analysis Tool is designed to process various document types (PDF, images) using Optical Character Recognition (OCR) and advanced AI-powered name extraction and analysis.


## 🎯 Purpose

The tool was created to solve complex document processing challenges:
- Extract names from various document types
- Perform intelligent text filtering
- Leverage AI for named entity recognition
- Provide flexible processing and analysis options

## 🚀 Key Features

- Multi-format document processing (PDF, PNG, JPG)
- Concurrent file processing
- Intelligent name extraction
- Google Gemini AI integration for advanced analysis
- Configurable text filtering
- Flexible output and saving options

## 🛠 Prerequisites

### Software Requirements
- Python 3.8+
- Tesseract OCR
- Google Gemini API Key

### Required Python Packages
- pytesseract
- pillow
- pdfplumber
- tqdm
- google-generativeai
- rapidfuzz

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
3. Configure Tesseract OCR

    - Download and install Tesseract OCR
    - Update path in `extractor.py` or `config.json` or both


    - Set up Google Gemini API Key


    - Add your API key in `config.json`

4. Set up PostgreSQL:

    - Create a database using the config in `config.json`.

5. Update the `config.json` file with your desired settings.

## Configuration (`config.json`)

- `remove_terms`: Words to filter out
- `google_gemini_api_key`: Your Gemini API key
- `output_format`: Desired output format
- `db_config`: Optional database configuration
- `batch_processing`: Multithreading settings

### Tests & Usage

### Run unit tests:

```bash
python -m unittest discover tests
```

### Run the script:
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

## Workflow
1. Select a folder containing documents
2. Tool extracts names from documents
3. Interactive options:
    - Perform Gemini AI analysis
    - Skip files
    - Save results
    - Exit program


## 🔮 Roadmap: Future Improvements

**Phase 1: Core Functionality Enhancements**
- Improve regex-based name extraction
- Add more robust error handling
- Enhance logging mechanisms
- Create comprehensive unit tests

**Phase 2: Advanced AI Integration**

- Support multiple AI models (OpenAI, Anthropic)
- Implement context-aware name extraction
- Add sentiment and professional context analysis
- Create custom training datasets

**Phase 3: Performance and Scalability**

- Optimize concurrent processing
- Add distributed computing support
- Implement caching mechanisms
- Create web/API interfaces

**Phase 4: Advanced Features**

- Machine learning model for improved extraction
- Support more document formats
- Real-time processing capabilities
- Advanced visualization of extracted data

## Contributing

### Contributions are always welcome!
### Please adhere to this project's `code of conduct`.

1. Fork the repository.

2. Create a feature branch:
```bash
git checkout -b feature-name
```

3. Commit changes:
```bash
git commit -m "Add feature description"
```

4. Push to your fork and submit a pull request.

If you have any questions or suggestions, feel free to contact me.

## ⚠️ Limitations

### Accuracy depends on document quality
### Requires stable internet for AI analysis
### Limited by Google Gemini API quotas

## 🙏 Acknowledgements

 - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
 - [Google Gemini AI](https://developers.google.com/learn/pathways/solution-ai-gemini-getting-started-web)

