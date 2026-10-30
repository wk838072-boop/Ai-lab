import csv, json, time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
from task2_chunks import make_chunks
def good_ranks(row, chunks, q):
    top = np.argsort(-row, kind="stable")[:3]
    return [rank for rank, i in enumerate(top, 1) if chunks[i]["doc"] == q["doc"] and q["evidence"] in chunks[i]["text"]]
def evaluate(scores, chunks, items):
    hits, reciprocal = [], []
    for row, q in zip(scores, items):
        if q["doc"] is None:
            continue
        good = good_ranks(row, chunks, q)
        hits.append(bool(good))
        reciprocal.append(1 / good[0] if good else 0)
    if not hits:
        return None, None
    return float(np.mean(hits)), float(np.mean(reciprocal))
def main():
    with open("corpus.json", encoding="utf-8") as f:
        docs = json.load(f)
    with open("queries.json", encoding="utf-8") as f:
        items = json.load(f)
    assert docs and items
    for q in items:
        assert q["split"] in {"dev", "test"}
        if q["doc"] is not None:
            assert q["evidence"] and q["evidence"] in docs[q["doc"]]
    t = time.perf_counter()
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    print("Model load seconds", time.perf_counter() - t)
    query_texts = [q["query"] for q in items]
    logs = []
    results = {}
    failures = []
    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(docs, strategy)
        texts = [c["text"] for c in chunks]
        lengths = [len(model.tokenizer(x, truncation=False)["input_ids"]) for x in texts + query_texts]
        print("Strategy", strategy, "longest input in tokens:", max(lengths), "limit:", model.max_seq_length)
        if max(lengths) > model.max_seq_length:
            raise ValueError("Model limit exceeded; rechunk or shorten query")
        for method in ["tfidf", "embedding"]:
            t = time.perf_counter()
            if method == "tfidf":
                vectorizer = TfidfVectorizer()
                C = vectorizer.fit_transform(texts)
                Q = vectorizer.transform(query_texts)
            else:
                C = model.encode(texts, normalize_embeddings=True)
                Q = model.encode(query_texts, normalize_embeddings=True)
            encode_seconds = time.perf_counter() - t
            t = time.perf_counter()
            scores = (Q @ C.T).toarray() if method == "tfidf" else Q @ C.T
            search_seconds = time.perf_counter() - t
            for split in ["dev", "test"]:
                indices = [i for i, q in enumerate(items) if q["split"] == split]
                result = evaluate(scores[indices], chunks, [items[i] for i in indices])
                results[(strategy, method, split)] = result
                print(strategy, method, split, "Hit@3/MRR@3", result, "chunks", len(chunks), "encode seconds", round(encode_seconds, 4), "search seconds", round(search_seconds, 6))
            for row, q in zip(scores, items):
                top = np.argsort(-row, kind="stable")[:3]
                if q["doc"] is not None and not good_ranks(row, chunks, q):
                    failures.append((strategy, method, q["query"], chunks[top[0]]["id"], chunks[top[0]]["text"]))
                for rank, i in enumerate(top, 1):
                    c = chunks[i]
                    record = dict(strategy=strategy, method=method, query=q["query"], split=q["split"], rank=rank, score=float(row[i]), chunk_id=c["id"], doc=c["doc"], start=c["start"], end=c["end"], text=c["text"], answerable=q["doc"] is not None)
                    logs.append(record)
                    print(strategy, method, q["query"], rank, round(record["score"], 3), c["id"], c["start"], c["end"], c["text"])
    with open("retrieval_log.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(logs[0]))
        writer.writeheader()
        writer.writerows(logs)
    print()
    print("Failures (answerable queries with no relevant chunk in the top three):")
    for strategy, method, query, chunk_id, text in failures:
        print(strategy, method, "|", query, "| top result:", chunk_id, "|", text)
    best = max([(s, m) for s in ["0", "10", "sentence"] for m in ["tfidf", "embedding"]], key=lambda k: (results[(k[0], k[1], "dev")][1], results[(k[0], k[1], "dev")][0]))
    print()
    print("Best on development data:", best, results[(best[0], best[1], "dev")])
    print("Same configuration on test data:", results[(best[0], best[1], "test")])
    print("Unanswerable queries still return text because retrieval always ranks the closest chunks, a high score does not prove the answer exists.")
if __name__ == "__main__":
    main()
