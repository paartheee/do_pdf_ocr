
# PDF Text and Table Extractor using PDF Plumber OCR

This project is a PDF Text and Table Extractor application built using Streamlit, pdfplumber, ocrmypdf, and Pandas. It allows users to upload a PDF file and extract the text and tables from it. If the PDF is an image-based PDF (non-searchable), the application performs OCR (Optical Character Recognition) to make the text searchable and then extracts the text and tables from the PDF. The extracted tables are converted into Markdown format for display.

## Features
- PDF Upload: Users can upload a PDF file through the Streamlit interface.
- OCR Processing: Automatically applies OCR to PDFs that do not have selectable text.
- Text and Table Extraction: Extracts both plain text and tables from the uploaded PDF file.
- Table Conversion to Markdown: Any table detected in the PDF is extracted and displayed in Markdown format.
## Requirements
To run this application, ensure you have the following packages installed:

- Python 3.8+ with WSL
- Streamlit: For creating the web interface.
- pdfplumber: For extracting text and tables from PDF files.
- ocrmypdf: For applying OCR to non-searchable PDFs.
- Pandas: For handling table extraction and formatting.
- PyPDF2: A PDF manipulation library used for reading and writing PDF files.
  
## Install Dependencies
To install the required dependencies, run:

``` bash
pip3 install streamlit pdfplumber ocrmypdf pandas PyPDF2
```
You may also need to install Tesseract OCR for ocrmypdf. You can follow the instructions on the Tesseract GitHub repository for installation based on your operating system.

## Usage

Clone or download this repository to your local machine.
Install the required dependencies listed above.
Run the Streamlit application using the following command:
```bash
streamlit run pdfplumber_app.py
```
Open your browser, and you should see the Streamlit interface. Upload a PDF file, and the app will display the extracted text and tables.


## Project Structure

├── pdfplumber_app.py - main file to run the application                                                              
├── README.md - The documentation
├── requirements.txt - the requirements library installation
├── plumber - Main Components of the pdfplumber OCR Code                                                           

## Code Explanation
### **preprocess_pdf()** Function:

This function processes the uploaded PDF. If the PDF does not have selectable text (e.g., it's a scanned image), OCR is performed using ocrmypdf to extract the text.
It returns a BytesIO object containing the OCR-processed PDF.
### **do_ocr_onpdf()** Function:

This function uses pdfplumber to extract both text and tables from the OCR-processed PDF.
Tables are detected, extracted into a Pandas DataFrame, and converted to Markdown format.
### **main()** Function:

This is the main Streamlit app where users upload a PDF file. The PDF is processed using the preprocess_pdf function, and the text and tables are extracted using the do_ocr_onpdf function.

## Example Workflow
- A user uploads a PDF file (either text-based or image-based).
- If the PDF is image-based, OCR is applied to recognize the text.
- The text and any tables are extracted and displayed in the app.
- Tables are formatted in Markdown and shown in the output alongside the plain text.
