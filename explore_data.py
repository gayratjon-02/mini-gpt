from pathlib import Path

text = Path("data/input.txt").read_text(encoding="utf-8")
chars = sorted(set(text))

print("matn uzunligi:", len(text))
print("noyob belgilar soni:", len(chars))
print(repr("".join(chars)))
 