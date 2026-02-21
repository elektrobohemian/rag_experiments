from load_data import load_documents
from clean_data import clean_text

def prepare_docs(folder_path="data/"):
    """
    Loads and cleans all text documents from the given folder.
    """
    # Load Documents
    raw_docs = load_documents(folder_path)

    # debug
    #print(f"DEBUG - Raw documents:")
    #for doc in raw_docs:
    #    print(f"\t{doc}")

    # Clean Documents
    cleaned_docs = [clean_text(doc) for doc in raw_docs]

    # debug
    #print(f"\n* * * * * * *\nDEBUG - Cleaned documents:")
    #for doc in cleaned_docs:
    #    print(f"\t{doc}")

    print(f"\tPrepared {len(cleaned_docs)} documents.")
    return cleaned_docs