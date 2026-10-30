import json
from pathlib import Path
from docs_data import DOCS, EVIDENCE
questions = [
    ("What is required for illness extensions?", "late", "dev"),
    ("How do I reset a forgotten password?", "password", "dev"),
    ("Where do I upload assignments?", "assignment", "dev"),
    ("Can contractors work remotely?", "contractor", "dev"),
    ("What do I do for blank printer pages?", "printer", "test"),
    ("How can I recover my login access?", "password", "test"),
    ("How should I hand in my coursework?", "assignment", "test"),
    ("What proof is needed when I was ill?", "late", "test"),
    ("What are tomorrow's flight prices?", None, "test"),
    ("Who won the football match?", None, "test")]
queries = [dict(query=q, doc=doc, evidence=EVIDENCE[doc] if doc else None, split=split) for q, doc, split in questions]
for name, data in [("corpus.json", DOCS), ("queries.json", queries)]:
    if Path(name).exists():
        raise FileExistsError("Refusing to overwrite " + name)
    Path(name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Created corpus.json and queries.json")
