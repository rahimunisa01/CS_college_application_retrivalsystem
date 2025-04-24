from scripts.indexer import build_index
# from sklearn.metrics.pairwise import cosine_similarity # (For TF-IDF)
import numpy as np
import re
from datetime import datetime
from dateutil.parser import parse
import math

# Old code using TF-IDF for search and cosine similarity
'''
# Extract and format multiple valid full-form deadline dates per document
def extract_deadline_snippets(text, n=5):
    date_pattern = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s*\d{4}|\d{1,2}/\d{1,2}/202[4-6]"
    seen = set()
    matched = []

    for line in text.split('\n'):
        found_dates = re.findall(date_pattern, line)
        for full_match in found_dates:
            clean = full_match.strip()
            if clean not in seen:
                matched.append(clean)
                seen.add(clean)
        if len(matched) >= n:
            break

    return matched if matched else ["No clear deadline found."]


def search(query, top_k=5):
    vectorizer, vectors, docs = build_index()
    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, vectors).flatten()
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for i in top_indices:
        doc = docs[i]
        summary = "\n".join(extract_deadline_snippets(doc["text"]))
        results.append({
            "title": doc["title"],
            "summary": summary,
            "score": float(scores[i])
        })
    return results
'''

# New code using BM25 for search and recency weighting
def extract_deadline_snippets(text, n=5):
    date_pattern = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s*\d{4}|\d{1,2}/\d{1,2}/202[4-6]"
    seen, matched = set(), []
    for line in text.split("\n"):
        for full_match in re.findall(date_pattern, line):
            clean = full_match.strip()
            if clean not in seen:
                matched.append(clean)
                seen.add(clean)
        if len(matched) >= n:
            break
    return matched if matched else ["No clear deadline found."]



def recency_weight(doc_date, now=None, decay=0.01):
    now = now or datetime.now()
    doc_dt = datetime.fromisoformat(doc_date)
    days_old = (now - doc_dt).days
    return math.exp(-decay * days_old)



def search(query, top_k=5, decay=0.01):
    bm25, docs = build_index()
    bm25_scores = bm25.get_scores(query.split()).flatten()  # array of length n_docs

    # compute recency weights
    now = datetime.now()
    recency_weights = []
    for doc in docs:
        snippets = extract_deadline_snippets(doc["text"])
        dates = []
        for snippet in snippets:
            date_str = snippet.strip()
            try:
                dates.append(parse(date_str))
            except Exception:
                continue

        if dates:
            # use latest date
            latest = max(dates)
            days_old = (now - latest).days
            weight = math.exp(-decay * days_old)
        else:
            # fallback weight to discourage results with no deadline?
            weight = 0.1

        recency_weights.append(weight)

    recency_weights = np.array(recency_weights)
    scores = bm25_scores * recency_weights
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for i in top_indices:
        doc = docs[i]
        snippets = extract_deadline_snippets(doc["text"])
        summary = "\n".join(f"👉 {s}" for s in snippets)
        results.append({
            "title":   doc["title"],
            "summary": summary,
            "score":   float(scores[i])
        })
    return results