from transformers import AutoTokenizer, AutoModel

def load_model(model_name):
    # Load the specified model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    return tokenizer, model
