import time
import streamlit as st
import os
import pandas as pd
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"  # Fallback setting for MPS if needed
from marker.convert import convert_single_pdf
from marker.logger import configure_logging
from marker.models import load_all_models

configure_logging()

def save_text_to_file(extracted_text, filename="extracted_text.txt"):
    """Saves the extracted text to a txt file."""
    with open(filename, "w") as f:
        f.write(extracted_text)

def display_metadata_as_dataframe(out_meta):
    """Convert the out_meta dictionary into a more structured DataFrame."""
    if isinstance(out_meta, dict):
        # Convert metadata dictionary into a DataFrame for better visualization
        df = pd.DataFrame.from_dict(out_meta, orient='index').reset_index()
        df.columns = ['Key', 'Value']  # Rename columns for clarity
        
        # Ensure all items in the 'Value' column are Arrow-compatible
        df['Value'] = df['Value'].apply(lambda x: ', '.join(map(str, x)) if isinstance(x, list) else str(x))
        
        return df
    else:
        return None

def extract_text_from_pdf(uploaded_file, model_lst):
    """Extracts text, images, and metadata from a single PDF."""
    full_text, images, out_meta = convert_single_pdf(
        uploaded_file, 
        model_lst, 
        max_pages=20, 
        batch_multiplier=2, 
        start_page=None, 
        ocr_all_pages=True
    )
    return full_text, images, out_meta

def main():
    """Streamlit app to upload multiple PDFs and display extracted text, images, and metadata."""
    
    st.title("Text and Table Extractor From PDF File Using Marker OCR")

    # Allow multiple PDF file uploads
    uploaded_files = st.file_uploader("Upload PDF files:", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        try:
            total_files = len(uploaded_files)  # Get the total number of files
            progress_bar = st.progress(0)
            model_lst = load_all_models()
            for idx, uploaded_file in enumerate(uploaded_files):
                with st.spinner(f"Processing File {idx + 1}/{total_files}: {uploaded_file.name}..."):
                    start_time = time.time()
                    # Simulate a delay to show the spinner
                    time.sleep(2)
                    st.subheader(f"Processing File {idx+1}: {uploaded_file.name}")
                    
                    # Extract text, images, and metadata from the PDF
                    full_text, images, out_meta = extract_text_from_pdf(uploaded_file, model_lst)
                    processing_time = time.time() - start_time  # End time - start time

                    st.text(f"Extracted Text from {uploaded_file.name} (Processed in {processing_time:.2f} seconds):")
                    # Display the extracted full text with page numbers
                    st.subheader(f"Extracted Text from {uploaded_file.name}:")
                    
                    # Handle page numbers in text
                    if isinstance(full_text, dict):  # If text is per-page
                        complete_text = ""
                        for page_num, page_text in full_text.items():
                            complete_text += f"\n--- Page {page_num} ---\n{page_text}\n"
                        st.text_area(f"Full Text - {uploaded_file.name}", value=complete_text, height=1000)
                        
                        
                        # Save extracted text to a .txt file with page numbers
                        save_text_to_file(complete_text, f"{uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")        
                        st.success(f"Text saved to {uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")
                        print(f"Text saved to {uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")

                        
                    elif isinstance(full_text, str):  # If it's a single string
                        st.text_area(f"Full Text - {uploaded_file.name}", value=full_text, height=1000)
                        
                        # Save extracted text to a .txt file
                        save_text_to_file(full_text, f"{uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")
                        st.success(f"Text saved to {uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")
                        print(f"Text saved to {uploaded_file.name.replace('.pdf', '')}_extracted_text.txt")
                        
                    # Display the extracted images
                    st.subheader("Extracted Images:")
                    if images:
                        for image_key, image_obj in images.items():
                            # Display each image using st.image
                            st.image(image_obj, caption=f"Image {image_key} from {uploaded_file.name}", use_column_width=True)
                    else:
                        st.write("No images extracted.")
        
                    # Display the extracted metadata in a clear DataFrame
                    st.subheader("Metadata:")
                    metadata_df = display_metadata_as_dataframe(out_meta)
                    if metadata_df is not None:
                        st.dataframe(metadata_df)  # Display metadata as a DataFrame
                    else:
                        st.write("No metadata available.")
                
                
                progress_bar.progress((idx + 1) / total_files)

        except Exception as e:
            st.error(f"Error processing file: {e}")
            print(e)

if __name__ == "__main__":
    main()
