#  Copyright (c) David Zellhöfer 2026.
#
#  Licensed under MIT License.

# models are cached at ~/.cache/huggingface
current_models = {
    #'SENTENCE_TRANSFORMER': 'T-Systems-onsite/cross-en-de-roberta-sentence-transformer', # not compatible!
    #'SENTENCE_TRANSFORMER': 'sentence-transformers/all-MiniLM-L6-v2', # all-purpose 384 dimensions model; 22.7M parameters
    # 'SENTENCE_TRANSFORMER': 'sentence-transformers/all-mpnet-base-v2', # 768 dimensions; 0.1B parameters
    #'SENTENCE_TRANSFORMER': 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2', # 768 dimensions; 0.3B parameters
    'SENTENCE_TRANSFORMER':'sentence-transformers/LaBSE', # multilingual model, 0.5B parameters
    #'SENTENCE_TRANSFORMER':'sentence-transformers/paraphrase-multilingual-mpnet-base-v2', # multilingual model, 768 dimensions; 0.3B parameters
    'LLM_ANSWER_GENERATION': 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    #'LLM_ANSWER_GENERATION': 'meta-llama/Llama-3.2-3B-Instruct',
    #'LLM_ANSWER_GENERATION': 'meta-llama/Meta-Llama-3.1-8B-Instruct',
}
