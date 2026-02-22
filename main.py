# based on https://www.kdnuggets.com/7-steps-to-build-a-simple-rag-system-from-scratch by Kanwal Mehreen
# edited by David Zellhöfer to ensure operativeness in 2026
import pickle

# Data preparation
from prepare_data import prepare_docs
from split_text import split_docs

# Embedding and storage
from create_embeddings import get_embeddings
from store_faiss import build_faiss_index, save_metadata

# Retrieval and answer generation
from generate_answer import generate_answer


def run_full_pipeline():
    """
    Runs the full end-to-end RAG workflow.
    """
    print("\nLoad and Clean Data:")
    documents = prepare_docs("data/")
    print(f"\tLoaded {len(documents)} clean documents.\n")

    print("Split Text into Chunks:")
    # documents is a list of strings, but split_docs expects a list of documents
    # For this simple example where documents are small, we pass them as strings
    chunks_and_metadata = split_docs(documents, chunk_size=500, chunk_overlap=100)
    # In this case, chunks_and_metadata is a list of tuples of LangChain Document objects and file names

    #tchunks_as_text=[]
    #for chunk in chunks_and_metadata:
    #    tchunks_as_text.append(chunk[0])
    #    print(chunk[0])
    # Debug
    sample_chunk=chunks_and_metadata[0]
    print(f"Sample contains the following keys: {sample_chunk.metadata.keys()}")

    # Extract only text content from LangChain Document objects
    texts = [c.page_content for c in chunks_and_metadata]
    print(f"\tCreated {len(texts)} text chunks.\n")

    print("Generate Embeddings:")

    text_parts = []
    for t in texts:
        text_parts.append(t[0])

    embeddings = get_embeddings(text_parts)

    print("Store Embeddings in FAISS:")
    index = build_faiss_index(embeddings)
    save_metadata(texts,chunks_and_metadata)
    print("Stored embeddings and metadata successfully.\n")

    answer_question()

def answer_question(top_k=3):
    print("Retrieve & Generate Answer:")
    # query = "Does unsupervised ML cover regression tasks?"
    query = "Wer ist David Zellhöfer?"
    #query = "Wer ist Berit Adam?"
    #query = "Wer ist Eric Kraatz?"
    generate_answer(query,top_k=top_k)

if __name__ == "__main__":
    # run the full pipeline
    run_full_pipeline()
    # run only the answer generation
    #answer_question()

    # DEBUG
    #print("\nFinished.\n* * * * *\n")
    #r=pickle.load(open("faiss_metadata.pkl", "rb"))
    #print(r)