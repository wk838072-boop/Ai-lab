import re
def word_spans(text):
    return [(m.start(), m.end()) for m in re.finditer(r"\S+", text)]
def windows(text, size=40, overlap=10, offset=0):
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("Require size > 0 and 0 <= overlap < size")
    spans = word_spans(text)
    result = []
    for i in range(0, len(spans), size - overlap):
        j = min(i + size, len(spans))
        result.append((offset + spans[i][0], offset + spans[j - 1][1]))
        if j == len(spans):
            break
    return result
def sentence_chunks(text, size=40):
    if size <= 0:
        raise ValueError("size must be positive")
    cuts = [0] + [m.end() for m in re.finditer(r"[.!?]\s+", text)] + [len(text)]
    out, pending, count = [], None, 0
    for a, b in zip(cuts, cuts[1:]):
        segment = text[a:b]
        n = len(segment.split())
        if not n:
            continue
        if n > size:
            if pending is not None:
                out.append(pending)
            out.extend(windows(segment, size, 0, a))
            pending, count = None, 0
        elif pending is not None and count + n <= size:
            pending, count = (pending[0], b), count + n
        else:
            if pending is not None:
                out.append(pending)
            pending, count = (a, b), n
    if pending is not None:
        out.append(pending)
    return out
def make_chunks(docs, strategy):
    result = []
    for doc_id, text in docs.items():
        spans = sentence_chunks(text) if strategy == "sentence" else windows(text, 40, int(strategy))
        for i, (a, b) in enumerate(spans):
            result.append(dict(id=f"{doc_id}:{i}", doc=doc_id, start=a, end=b, text=text[a:b]))
    return result
if __name__ == "__main__":
    from docs_data import DOCS, PAIRS
    assert windows("") == []
    assert sentence_chunks("") == []
    assert windows("short text") == [(0, 10)]
    assert sentence_chunks("short text") == [(0, 10)]
    try:
        windows("a b", 2, 2)
    except ValueError:
        print("Invalid overlap raised ValueError")
    else:
        raise AssertionError("Invalid overlap was accepted")
    long = " ".join(["word"] * 95) + "."
    pieces = sentence_chunks(long)
    assert all(len(long[a:b].split()) <= 40 for a, b in pieces)
    print("95 word sentence split into", len(pieces), "fallback windows")
    docs = {name: DOCS[name] for name in ["late", "password", "contractor"]}
    for name, text in docs.items():
        print(name, "words:", len(text.split()))
    for strategy in ["0", "10", "sentence"]:
        print()
        print("Strategy:", strategy)
        chunks = make_chunks(docs, strategy)
        for c in chunks:
            assert c["text"] == docs[c["doc"]][c["start"]:c["end"]]
        sizes = [len(c["text"].split()) for c in chunks]
        original = sum(len(t.split()) for t in docs.values())
        print("Chunks:", len(chunks), "| smallest:", min(sizes), "| largest:", max(sizes), "| average:", round(sum(sizes) / len(sizes), 1))
        print("Repeated words:", sum(sizes) - original)
        for name, (rule, exception) in PAIRS.items():
            together = any(rule in c["text"] and exception in c["text"] for c in chunks if c["doc"] == name)
            print(name, "rule and exception in one chunk:", together)
    print()
    tricky = "Dr. Khan approved the request. The deadline is Friday."
    for a, b in sentence_chunks(tricky, 4):
        print("Abbreviation test:", repr(tricky[a:b]))
    print("The splitter cuts after Dr. because it treats the dot as a sentence end.")
