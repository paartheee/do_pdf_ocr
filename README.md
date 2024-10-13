# Text and Table Extractor From PDF Using Marker OCR and PDFPlumber OCR
## Problem Statement
Extracting text and tables from PDF files that contain a mix of searchable text and scanned images (image-based PDFs) presents significant challenges in accurately retrieving content. Standard OCR (Optical Character Recognition) tools often struggle with complex document structures, such as embedded tables, metadata, and images. These tools may produce inconsistent text recognition, poorly handle tables, and fail to extract essential data like metadata and images, leading to incomplete or inaccurate results.

This repository addresses these issues by offering a comprehensive solution for processing PDFs and extracting text, tables, images, and metadata using two powerful methods:

- Marker OCR: Best suited for extracting text, images, and metadata from PDFs, offering advanced capabilities for handling non-searchable documents.
- PDFPlumber: Specialized in extracting tables and text, with OCR functionality to process scanned image-based PDFs and accurately capture tables and text.

By combining these two approaches, this solution enables precise extraction of both text and structured data (such as tables) from a variety of PDF document types.

The repository provides a complete solution for extracting text and tables from PDFs, whether they are text-based or image-based (scanned). It integrates two powerful OCR and PDF processing tools—Marker OCR and PDFPlumber OCR—to handle diverse types of PDFs and deliver comprehensive extraction capabilities. The application is built using Streamlit, offering a user-friendly web interface.

## Features
- PDF Upload: Users can upload PDFs via the Streamlit interface.
- Text Extraction: Extracts and displays text content from uploaded PDFs.
- Table Extraction: Extracts and converts tables from the PDF into structured formats, including Markdown.
- Image Extraction (Marker OCR): Extracts and displays images embedded in the PDF.
- Metadata Extraction (Marker OCR): Extracts and displays document metadata (e.g., author, creation date) in a DataFrame format.
- OCR Processing: Automatically applies OCR to non-searchable, image-based PDFs using either Marker OCR or PDFPlumber.
- Interactive UI: Provides a user-friendly interface that allows easy navigation and presentation of extracted data.

## Prerequisites
To run this application, you need the following:

- Python 3.8 or later
- Streamlit: For creating the web interface.
- Marker OCR: For advanced OCR processing, image, and metadata extraction.
- PDFPlumber: For extracting text and tables from PDFs.
- OCRmyPDF: For applying OCR to non-searchable, image-based PDFs.
- Pandas: For handling table extraction and metadata formatting.
- PyPDF2: A PDF manipulation library used for reading PDF files.

## Installing Dependencies
- To install the required dependencies, run the following:

``` bash
pip install streamlit marker pdfplumber ocrmypdf pandas PyPDF2 torch torchvision torchaudio
```
Ensure you have Tesseract OCR installed for OCRmyPDF. You can find installation instructions on the Tesseract GitHub.

## How to Run the App
- Clone or Download the repository to your local machine.
- Install the required dependencies (see above).
- Launch the Streamlit app by running:
``` bash
streamlit run app.py
```
Open your browser and upload a PDF file to extract text, images, tables, and metadata.

## Example Workflow
- Upload a PDF: The app allows users to upload either a text-based or an image-based PDF.
- OCR Processing: If the PDF is image-based, OCR is performed to make the text searchable.
- Text & Table Extraction: The app extracts text and tables from the PDF, displaying text in a scrollable box and tables in Markdown format.
- Image Extraction (Marker OCR): Displays any images found in the PDF, along with captions.
- Metadata (Marker OCR): Metadata is displayed in a structured DataFrame format.

## Project Structure

├── app.py - Main file to run the application
├── README.md - The documentation
├── requirements.txt - The dependencies for the application
├── marker - Components for Marker OCR extraction
├── plumber - Components for PDFPlumber OCR extraction


## Key Functions
### Marker OCR Functions
- convert_single_pdf(): Uses the Marker OCR library to extract text, images, and metadata from the PDF.
- display_metadata_as_dataframe(out_meta): Converts extracted metadata into a DataFrame for easy reading.
### PDFPlumber Functions
- preprocess_pdf(): Processes an uploaded PDF. If it's image-based, OCR is applied.
- do_ocr_onpdf(): Extracts text and tables from the PDF using PDFPlumber and formats tables into Markdown.
### Error Handling 
The app is built with robust error handling to manage issues like unsupported PDF formats, missing dependencies, and file processing errors. Errors are caught and displayed using st.error() in the Streamlit UI.










