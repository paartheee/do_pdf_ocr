import streamlit as st
from plumber.preprocess_pdf import preprocess_pdf
from plumber.do_ocr_onpdf import do_ocr_onpdf

def save_text_to_file(extracted_text, filename="extracted_text.txt"):
    """Saves the extracted text to a txt file."""
    with open(filename, "w") as f:
        f.write(extracted_text)




def main():
    """Streamlit app to upload PDF and display extracted text."""

    st.title("Text and Table Extractor From PDF File using PDF Plumber OCR.")

    # Allow PDF file upload
    uploaded_file = st.file_uploader("Upload PDF file:", type="pdf")

    if uploaded_file is not None:
        try:
            # Process the PDF to extract text
            preprocessed_pdf = preprocess_pdf(uploaded_file)
            extracted_text = do_ocr_onpdf(preprocessed_pdf)

            # Check if the result is a string (entire document text) or a dictionary (page-by-page)
            if isinstance(extracted_text, str):
                # If it's a string, assume it's the entire document
                st.write("Extracted Text:")
                st.code(extracted_text, language="text")

                # Save extracted text to a .txt file
                save_text_to_file(extracted_text, "extracted_text.txt")
                st.success("Text saved to extracted_text.txt")
                print("Text saved to extracted_text.txt")
            
            else:
                st.error("Unexpected output format. Expected string but received something else.")

        except Exception as e:
            st.error(f"Error processing file: {e}")


if __name__ == "__main__":
    main()
