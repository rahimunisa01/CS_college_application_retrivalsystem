
from sklearn.feature_extraction.text import TfidfVectorizer
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
    corpus = [doc["text"] for doc in docs]
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(corpus)
    return vectorizer, vectors, docs