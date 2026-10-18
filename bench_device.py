import time
import torch


def bench(device, n=4096, repeats=10):
    a = torch.randn(n, n, device=device)
    b = torch.randn(n, n, device=device)

    for _ in range(3):  # isitish
        a @ b
    if device == "mps":
        torch.mps.synchronize()

    t0 = time.perf_counter()
    for _ in range(repeats):
        a @ b
    if device == "mps":
        torch.mps.synchronize()
    return (time.perf_counter() - t0) / repeats


for dev in ["cpu", "mps"]:
    print(f"{dev}: {bench(dev) * 1000:.1f} ms")
