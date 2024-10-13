# Text and Table Extractor From PDF Using Marker OCR
This project is a Streamlit app that allows users to upload a PDF file and extracts its content, including text, images, and metadata, using the Marker OCR and document processing library. The app then displays the extracted data in an interactive manner.

## Features
- PDF Upload: Upload a PDF file to the app.
- Text Extraction: Extract and display the full text content from the uploaded PDF.
- Image Extraction: Extract and display images embedded in the PDF.
- Metadata Extraction: Extract and display document metadata (such as author, creation date, etc.) in a clean DataFrame.
- Interactive UI: Use Streamlit’s features to create a user-friendly interface, displaying data in a readable format.

## Prerequisites
Before running the app, make sure you have the following installed:

- Python 3.8 or later
- Streamlit
- Marker OCR and document processing library
- Required dependencies for Marker OCR, including torch, PIL, and pandas
- Installing Dependencies
- Install the required Python packages using pip3:

```bash
pip3 install streamlit marker pandas
```
Additional Required Packages
The Marker package might require additional dependencies like torch. You can install torch using the following command if it's not already installed:

```bash
pip3 install torch torchvision torchaudio
```

Ensure you have the required dependencies, especially for GPU-based acceleration (MPS for Mac, CUDA for NVIDIA GPUs, etc.).

## How to Run the App
Clone or Download the Project: If you have the script saved in a file (e.g., marker_app.py), make sure you’re in the directory where the file is located.

Run the Streamlit App: Use the following command to launch the Streamlit app:

```bash
streamlit run marker_app.py
```
Upload a PDF: After launching, the app will open in your default web browser. Upload a PDF file to begin extracting text, images, and metadata.

## File Structure
Here's the structure of the main components:

├── marker_app.py - main file to run the application                                                              
├── README.md - The documentation
├── requirements.txt - the requirements library installation
├── marker - Main Components of the marker OCR Code     

1. PDF Upload
The app allows users to upload a PDF file through Streamlit's st.file_uploader(). The uploaded file is then processed using the Marker package.

2. Text Extraction
The extracted text is displayed using st.text_area() in a scrollable area. The height of the text area is set to allow easy reading of large documents.

3. Image Extraction
The images are extracted from the PDF and displayed using st.image(). Each image is captioned with its respective image key.

4. Metadata Extraction
Metadata extracted from the PDF is displayed in a structured DataFrame using st.dataframe(). This includes fields like author, creation date, etc.

## Key Functions:
convert_single_pdf(): This function is provided by the Marker library to perform OCR, extract images, text, and metadata from the uploaded PDF.

## display_metadata_as_dataframe(out_meta): Converts metadata into a more readable format (a pandas.DataFrame).

Error Handling:
Errors encountered during PDF processing (e.g., unsupported PDF formats, missing dependencies) are handled using a try-except block. If an error occurs, it is displayed using st.error().

### Usage Example

Start the app by running the streamlit run marker_app.py command.

- Upload a PDF file.
- The app will process the PDF and display the following:
- Extracted Text: A scrollable text box with all the text extracted from the PDF.
- Extracted Images: Any images in the PDF will be displayed with captions.
- Metadata: Document metadata will be displayed in an interactive table format.

## Example PDF Output:
- Text: A long string of extracted text.
- Images: If images are found, they will be displayed along with their image keys.
- Metadata: The metadata is displayed in a structured table format.