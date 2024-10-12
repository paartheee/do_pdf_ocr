import pdfplumber
import pandas as pd
import streamlit as st
from pdfplumber.utils import extract_text, get_bbox_overlap, obj_to_bbox
import io
import ocrmypdf



def preprocess_pdf(pdf_file):
    """Processes a PDF file and returns a BytesIO object of the OCR-processed PDF."""

    pdf_bytes = pdf_file.read()
    input_pdf_stream = io.BytesIO(pdf_bytes)

    # Create another BytesIO object to store the output in memory
    output_pdf_stream = io.BytesIO()

    # Perform OCR with DPI adjustment and other preprocessing options
    ocrmypdf.ocr(input_pdf_stream, output_pdf_stream, language='eng', skip_text=True, 
                 image_dpi=300, deskew=True)

    # After OCR, we need to seek back to the start of the BytesIO object before using pdfplumber
    output_pdf_stream.seek(0)
    return output_pdf_stream


def do_ocr_onpdf(preprocessed_pdf_file):
    """Extracts text and tables from the OCR-processed PDF using pdfplumber."""
    
    # Open the OCR-processed PDF using pdfplumber
    with pdfplumber.open(preprocessed_pdf_file) as pdf:
        all_text = []
        
        # Iterate through all pages in the PDF
        for page_num, page in enumerate(pdf.pages):
            filtered_page = page
            chars = filtered_page.chars

            # Find and process any tables on the page
            for table in page.find_tables():
                first_table_char = page.crop(table.bbox).chars[0]

                # Filter out table objects from page chars
                filtered_page = filtered_page.filter(lambda obj:
                    get_bbox_overlap(obj_to_bbox(obj), table.bbox) is None
                )

                chars = filtered_page.chars
                df = pd.DataFrame(table.extract())
                df.columns = df.iloc[0]
                markdown = df.drop(0).to_markdown(index=False)

                # Append table in markdown format as text
                chars.append(first_table_char | {"text": markdown})

            # Extract text from the page, including any tables
            page_text = extract_text(chars, layout=True)
            all_text.append(f"Page {page_num + 1}:\n{page_text}\n")

    # Join all the extracted text from all pages
    return "\n".join(all_text)


def main():
    """Streamlit app to upload PDF and display extracted text."""

    st.title("Text and Table Extractor From PDF File")

    # Allow PDF file upload
    uploaded_file = st.file_uploader("Upload PDF file:", type="pdf")

    if uploaded_file is not None:
        try:
            # Process the PDF to extract text
            preprocessed_pdf = preprocess_pdf(uploaded_file)
            extracted_text = do_ocr_onpdf(preprocessed_pdf)
            st.write("Extracted Text:")
            st.code(extracted_text, language="text")
        except Exception as e:
            st.error(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
