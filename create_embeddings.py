from sentence_transformers import SentenceTransformer
import numpy as np
from my_secrets import secrets
from model_setup import current_models as cm

def get_embeddings(text_chunks):
    HF_TOKEN = secrets.get('HF_TOKEN')
    # Load embedding model
    # models are cached at ~/.cache/huggingface
    model = SentenceTransformer(cm.get('SENTENCE_TRANSFORMER'), token=HF_TOKEN)

    print(f"Creating embeddings for {len(text_chunks)} chunks:")
    embeddings = model.encode(text_chunks, show_progress_bar=True)

    print(f"Embeddings shape: {embeddings.shape}")
    return np.array(embeddings)