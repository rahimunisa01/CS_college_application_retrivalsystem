# from sklearn.feature_extraction.text import TfidfVectorizer # (For TF-IDF)
from rank_bm25 import BM25Okapi
import json
import os

def load_documents(path="data/documents/docs.json"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Document file not found: {path}")
    with open(path, "r") as f:
        docs = json.load(f)
    if not docs:
        raise ValueError("No documents found in the file.")
    return docs

def build_index():
    docs = load_documents()
    print(f"Loaded {len(docs)} documents.")

    for doc in docs:
        text = doc["text"].lower()
        additions = []
        if "m.s.e." in text or "mse" in text:
            additions.append("computer science ms master's")
        if "eecs" in text:
            additions.append("computer science cs")
        if additions:
            doc["text"] += " " + " ".join(additions)

    corpus = [doc["text"].split() for doc in docs]
    bm25 = BM25Okapi(corpus)
    return bm25, docs

