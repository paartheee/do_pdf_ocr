
import re  # Import regular expressions for cleaning text

def clean_text(text):
    """Cleans the extracted text by removing unwanted repetitive characters."""
    # This regex removes sequences of more than 2 repeating characters
    cleaned_text = re.sub(r'(.)\1{2,}', r'\1', text)
    return cleaned_text

