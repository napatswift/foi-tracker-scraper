# foi-tracker-scraper

This project is designed to scrape PDF files from [oic](www.oic.go.th) website and download them to your local machine.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Setup

1. **Create a Python virtual environment**

```sh
python -m venv env
```

2. **Activate the virtual environment**

   - On Windows:
  
    ```sh
    .\env\Scripts\activate
    ```
  
   - On macOS and Linux:
  
    ```sh
    source env/bin/activate
    ```

3. Install the required dependencies

```
pip install -r requirements.txt
```

## Running the Scraper

1. **Run the spider crawler**

This command will run the spider defined in scraper.py and save the output to pdf_files.json.

```sh
scrapy runspider -O pdf_files.json scraper.py
```

1. **Download the PDFs**

After running the spider, you can download the PDFs using the download-pdf.py script.

```sh
python download-pdf.py
```
