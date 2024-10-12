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

def main():
    """Streamlit app to upload PDF and display extracted text, images, and metadata. u"""
    
    st.title("Text and Table Extractor From PDF File Using Marker OCR.")

    # Allow PDF file upload
    uploaded_file = st.file_uploader("Upload PDF file:", type="pdf")

    if uploaded_file is not None:
        try:
            model_lst = load_all_models()
            # Extract text, images, and metadata from the PDF
            full_text, images, out_meta = convert_single_pdf(
                uploaded_file, 
                model_lst, 
                max_pages=20, 
                batch_multiplier=2, 
                start_page=None, 
                ocr_all_pages=True
            )
            
            # Display the extracted full text
            st.subheader("Extracted Text:")
            st.text_area("Full Text", value=full_text, height=1000)
             # Check if the result is a string (entire document text) or a dictionary (page-by-page)
            if isinstance(full_text, str):
                # If it's a string, assume it's the entire document
                st.write("Extracted Text:")
                st.code(full_text, language="text")

                # Save extracted text to a .txt file
                save_text_to_file(full_text, "extracted_text.txt")
                st.success("Text saved to extracted_text.txt")
                print("Text saved to extracted_text.txt")
            # Display the extracted images
            st.subheader("Extracted Images:")
            if images:
                for image_key, image_obj in images.items():
                    # Display each image using st.image
                    st.image(image_obj, caption=f"Image {image_key}", use_column_width=True)
            else:
                st.write("No images extracted.")

            # Display the extracted metadata in a clear DataFrame
            st.subheader("Metadata:")
            metadata_df = display_metadata_as_dataframe(out_meta)
            if metadata_df is not None:
                st.dataframe(metadata_df)  # Display metadata as a DataFrame
            else:
                st.write("No metadata available.")

        except Exception as e:
            st.error(f"Error processing file: {e}")
            print(e)

if __name__ == "__main__":
    main()
