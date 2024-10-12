

import pdfplumber
import pandas as pd
from pdfplumber.utils import extract_text, get_bbox_overlap, obj_to_bbox
import json 
from plumber.clean_text import clean_text


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



