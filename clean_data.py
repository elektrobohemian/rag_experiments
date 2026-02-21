import re

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text) # replaces multiple whitespaces characters by one
    # the original line only matches basic Latin Unicode characters which would only work for English texts
    # every character that is not plain ASCII gets replaced by ' '
    # text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # as we want to support most languages as well, we have to include all valid Unicode alphanumeric characters,
    # i.e. the \w class, or short we replace its complement (\W) with ' ' but this would also remove characters such as
    # @ or the like, so we skip this `cleansing' step as is demolishes the strings.
    # see https://www.utf8-chartable.de/unicode-utf8-table.pl?number=128&utf8=string-literal
    # text = re.sub(r'[\W]+', ' ', text)

    return text.strip()