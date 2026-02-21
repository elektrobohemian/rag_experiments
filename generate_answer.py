from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from retrieve_faiss import load_faiss_index, load_metadata, retrieve_similar_chunks
from my_secrets import secrets

def generate_answer(query, top_k=3):
    """
    Retrieves relevant chunks and generates a final answer.
    """

    HF_TOKEN = secrets.get('HF_TOKEN')

    # Load FAISS index and metadata
    index = load_faiss_index()
    text_chunks = load_metadata()

    # Retrieve top relevant chunks
    context_chunks = retrieve_similar_chunks(query, index, text_chunks, top_k=top_k)
    context = "\n\n".join(context_chunks)

    # Load open-source LLM
    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    print(f"Loading LLM: {model_name}")

    # Load tokenizer and model, using a device map for efficient loading
    tokenizer = AutoTokenizer.from_pretrained(model_name)
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

    # Generate output
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    # Use the correct input for model generation
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=200, pad_token_id=tokenizer.eos_token_id)

    # Decode and clean up the answer, removing the original prompt
    full_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Simple way to remove the prompt part from the output
    answer = full_text.split("Answer:")[1].strip() if "Answer:" in full_text else full_text.strip()

    print("\nFinal Answer:")
    print(answer)