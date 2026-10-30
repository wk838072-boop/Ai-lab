from guided_chatbot import build_bot
for backend in ["tfidf", "embedding"]:
    engine = build_bot(backend)
    for query in ["assignment upload", "forgot login"]:
        print("Backend:", backend, "| Query:", query)
        for record, score in engine.search(query, k=3):
            print("  ", record["question"], f"({score:.3f})")
