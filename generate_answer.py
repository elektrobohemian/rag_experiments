from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from retrieve_faiss import load_faiss_index, load_metadata, retrieve_similar_chunks
from my_secrets import secrets
from model_setup import current_models as cm

def generate_answer(query, top_k=3):
    """
    Retrieves relevant chunks and generates a final answer.
    """

    HF_TOKEN = secrets.get('HF_TOKEN')

    # Load FAISS index and metadata
    index = load_faiss_index()
    text_chunks = load_metadata()

    # Retrieve top relevant chunks
    #context_chunks = retrieve_similar_chunks(query, index, text_chunks, top_k=top_k)
    #context = "\n\n".join(context_chunks)

    # get the most similar chunks in form of a list of indices
    indices = retrieve_similar_chunks(query, index, text_chunks, top_k=top_k)

    # select the relevant text part and the related metadata with the help of the indices
    context_chunks=[text_chunks[0][i] for i in indices[0]]
    metadata_chunks=[text_chunks[1][i] for i in indices[0]]

    context = "\n\n".join(context_chunks)

    it=0
    print("Retrieved chunks:")
    for c in context_chunks:
        it+=1
        print(f"\t{it}.{metadata_chunks[it-1].metadata['file_name']}: {c}")

    # Load open-source LLM
    model_name = cm.get('LLM_ANSWER_GENERATION')
    print(f"\nLoading LLM: {model_name}")

    # Load tokenizer and model, using a device map for efficient loading
    tokenizer = AutoTokenizer.from_pretrained(model_name,token=HF_TOKEN)
    #model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto",
                                                 token=HF_TOKEN)  # removed torch_dtype=float16 due to deprecation warning

    # Build the prompt
    prompt = f"""
    Context:
    {context}
    Question:
    {query}
    Answer:
    """

    print("\nContext:")
    print(context)

    # Generate output
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    # Use the correct input for model generation
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=200, pad_token_id=tokenizer.eos_token_id)

    # Decode and clean up the answer, removing the original prompt
    full_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # debug
    #print(f"\tFull text:\n\t\t >{full_text}<\n")

    # Simple way to remove the prompt part from the output
    answer = full_text.split("Answer:")[1].strip() if "Answer:" in full_text else full_text.strip()

    print("\n* * * * * * * * * * * * * * * * * * *\nFinal Answer:\n")
    print(answer)
    print("Done.")