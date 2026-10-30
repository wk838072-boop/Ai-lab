import re
samples = ["AI, search!", "I can't log in.", "help@example.com", "CS4944 late!", "", "یہ ایک مثال ہے"]
for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print("Original:", repr(text))
    print("Whitespace:", ws, len(ws))
    print("Word-like:", words, len(words))
    print()
assert re.findall(r"\b\w+\b", "") == []
try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    for text in samples[:2]:
        tokens = model.tokenizer.tokenize(text)
        print("Model tokens:", repr(text), tokens, len(tokens))
except Exception as error:
    print("Model tokenizer not available:", error)
print()
print("Difference 1: split() keeps punctuation attached ('AI,' and 'search!') but the regex removes it.")
print("Difference 2: the regex splits can't into can and t and splits the email into pieces, split() keeps them whole.")
print("Normalization risk: removing punctuation or lowercasing can damage emails, identifiers like CS4944 and negations like can't.")
print("The regex is not a complete multilingual tokenizer.")
