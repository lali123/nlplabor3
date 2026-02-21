from sentence_transformers import SentenceTransformer

def get_embeddings(texts: list[str], model_name: str = 'all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts)
    return embeddings

# Usage: vectors = get_embeddings(["Logmein Resolve performance", "Data science at IK-TEOKJ"])
