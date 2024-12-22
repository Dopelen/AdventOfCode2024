from collections import Counter
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 41.txt"
file_path = os.path.join(desktop, file_name)

with (open(file_path, "r", encoding="utf-8") as file):
    data = file.read().split("\n")

    keyp = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
    dirp = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}


    def steps(G: dict[complex, str], s: str, i=1):
        px, py = G["A"]
        bx, by = G[" "]
        res = Counter()
        for c in s:
            npx, npy = G[c]
            f = npx == bx and py == by or npy == by and px == bx
            res[(npx - px, npy - py, f)] += i
            px, py = npx, npy
        return res


    def go(n):
        r = 0
        for code in data:
            res = steps(keyp, code)
            for _ in range(n + 1):
                res = sum((steps(dirp, ("<" * -x + "v" * y + "^" * -y + ">" * x)[:: -1 if f else 1] + "A", res[(x, y, f)]) for x, y, f in res), Counter())
            r += res.total() * int(code[:3])
        return r


print(go(2))

