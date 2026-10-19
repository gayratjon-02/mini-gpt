from pathlib import Path

text = Path("data/input.txt").read_text(encoding="utf-8")
chars = sorted(set(text))


stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}
def encode(s): return [stoi[c] for c in s]
def decode(ids): return "".join(itos[i] for i in ids)


print(encode("hii there"))
print(decode(encode("hii there")))
