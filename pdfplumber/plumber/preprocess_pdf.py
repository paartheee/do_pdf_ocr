
import io
import ocrmypdf



def preprocess_pdf(pdf_file):
    """Processes a PDF file and returns a BytesIO object of the OCR-processed PDF."""

    pdf_bytes = pdf_file.read()
    input_pdf_stream = io.BytesIO(pdf_bytes)

    # Create another BytesIO object to store the output in memory
    output_pdf_stream = io.BytesIO()

    # Perform OCR with DPI adjustment and other preprocessing options
    ocrmypdf.ocr(input_pdf_stream, output_pdf_stream, language='eng', skip_text=True, clean=True)

    # After OCR, we need to seek back to the start of the BytesIO object before using pdfplumber
    output_pdf_stream.seek(0)
    return output_pdf_stream


