import streamlit as st
from plumber.preprocess_pdf import preprocess_pdf
from plumber.do_ocr_onpdf import do_ocr_onpdf
import time  # Used to simulate a delay for loading in this example


def save_text_to_file(extracted_text, filename="extracted_text.txt"):
    """Saves the extracted text to a txt file."""
    with open(filename, "w") as f:
        f.write(extracted_text)


def main():
    """Streamlit app to upload PDF and display extracted text."""

    st.title("Text and Table Extractor From PDF File using PDF Plumber OCR.")

    # Allow PDF file upload
    uploaded_files = st.file_uploader("Upload PDF files:", type="pdf", accept_multiple_files=True)

    if uploaded_files is not None:
        try:
            total_files = len(uploaded_files)  # Get the total number of files
            progress_bar = st.progress(0)  # Initialize the progress bar

            for idx, uploaded_file in enumerate(uploaded_files):
                with st.spinner(f"Processing File {idx + 1}/{total_files}: {uploaded_file.name}..."):
                    # Simulate a delay to show the spinner
                    time.sleep(2)

                    # Process the PDF to extract text
                    preprocessed_pdf = preprocess_pdf(uploaded_file)
                    extracted_text = do_ocr_onpdf(preprocessed_pdf)

                    st.subheader(f"Extracted Text from {uploaded_file.name}:")
                    
                    # Handle page numbers in text
                    if isinstance(extracted_text, dict):  # If text is per-page
                        complete_text = ""
                        for page_num, page_text in extracted_text.items():
                            complete_text += f"\n--- Page {page_num} ---\n{page_text}\n"
                        st.text_area(f"Full Text - {uploaded_file.name}", value=complete_text, height=1000)
                        
                        # Save extracted text to a .txt file with page numbers
                        save_text_to_file(complete_text, f"{uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")        
                        st.success(f"Text saved to {uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")
                        print(f"Text saved to {uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")

                    elif isinstance(extracted_text, str):  # If it's a single string
                        st.text_area(f"Full Text - {uploaded_file.name}", value=extracted_text, height=1000)
                        
                        # Save extracted text to a .txt file
                        save_text_to_file(extracted_text, f"{uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")
                        st.success(f"Text saved to {uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")
                        print(f"Text saved to {uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")
                    
                    else:
                        st.error("Unexpected output format. Expected string but received something else.")

                # Update progress bar after each file is processed
                progress_bar.progress((idx + 1) / total_files)

        except Exception as e:
            st.error(f"Error processing file: {e}")


if __name__ == "__main__":
    main()
