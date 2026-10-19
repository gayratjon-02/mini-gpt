import torch
from pathlib import Path

text = Path("data/input.txt").read_text(encoding="utf-8")
chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
data = torch.tensor([stoi[c] for c in text], dtype=torch.long)

n = int(0.9 * len(data))
train_data = data[:n]
val_data = data[n:]

print(data.shape, data.dtype)
print(data[:20])
print(len(train_data), len(val_data))
