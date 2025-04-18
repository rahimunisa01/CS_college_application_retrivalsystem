# =====================================
# scripts/search.py (Fixed: full date extraction with findall)
# =====================================

from scripts.indexer import build_index
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

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
                matched.append(f"👉 {clean}")
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
