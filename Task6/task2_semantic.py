from docs_data import DOCS
from task2_chunks import make_chunks
from lab6_search import Retriever
docs = {name: DOCS[name] for name in ["late", "password", "contractor"]}
records = make_chunks(docs, "sentence")
queries = ["I was sick and need more time for my coursework", "How can I regain access to my account?", "Can a freelancer work from home?"]
for backend in ["tfidf", "embedding"]:
    engine = Retriever(records, backend)
    print("Backend:", backend)
    for query in queries:
        print("Query:", query)
        hits = engine.search(query, k=3)
        if not hits:
            print("No matching records.")
        for r, score in hits:
            print(r["id"], f"score={score:.3f}", "chars", r["start"], r["end"])
            print(r["text"])
        print()
