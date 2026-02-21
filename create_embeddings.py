from sentence_transformers import SentenceTransformer
import numpy as np
from my_secrets import secrets

def get_embeddings(text_chunks):
    HF_TOKEN = secrets.get('HF_TOKEN')
    # Load embedding model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2',token=HF_TOKEN)

    print(f"Creating embeddings for {len(text_chunks)} chunks:")
    embeddings = model.encode(text_chunks, show_progress_bar=True)

    print(f"Embeddings shape: {embeddings.shape}")
    return np.array(embeddings)