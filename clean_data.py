import re

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text) # Unicode control characters, see https://www.utf8-chartable.de/unicode-utf8-table.pl?number=128&utf8=string-literal
    return text.strip()