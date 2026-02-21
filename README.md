# rag_experiments
RAG experiments

## Prerequisites

You have to _manually__ create a file called ``my_secrets.py`` with the following content:
```
secrets = {
    'HF_TOKEN': "place_your_hugging_face_token_here"
}
```
In this file you will have to replace ``place_your_hugging_face_token_here`` with a [Hugging Face](https://huggingface.co) 
token of your own. Otherwise, the scripts will not work as expected.

You can find a sample file called [``my_secrets.py.sample``](./my_secrets.py.sample) that can be simply renamed to ``my_secrets.py``.

__ATTENTION:__ Do not call the file ``secrets.py`` or you will run into problems caused by numpy.