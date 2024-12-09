import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 18.txt"
file_path = os.path.join(desktop, file_name)
empty, still = {}, {}

with (open(file_path, "r", encoding="utf-8") as file):
    line = list(map(int, file.read()))
    size = len(line)
    for i in range(1, size, 2):
        empty[i] = [[], line[i]]
    id = (size // 2) - 1 + (size % 2)
    for index in range(size - 1 - (not (size % 2)), -1, -2):
        moved = False
        for key, val in empty.items():
            amount = line[index]
            if all([key < index, val[1], val[1] >= amount]):
                empty[key][0] += [id] * amount
                empty[key][1] -= amount
                moved = True
                break
        if not moved:
            still[index] = [id] * amount

        id -= 1
    pre_ans = []
    for e in range(size):
        if still.get(e):
            adit = still[e]
        elif e % 2:
            adit = empty[e][0] + [0] * empty[e][1]
        else:
            adit = [0] * line[e]
        pre_ans += adit

print(sum(a * ind for ind, a in enumerate(pre_ans)))
