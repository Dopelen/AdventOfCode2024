import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 49.txt"
file_path = os.path.join(desktop, file_name)
locks = []
keys = []
fit = 0

with open(file_path, "r", encoding="utf-8") as file:
    is_lock = file.readline() == "#####\n"
    pattern = [0] * 5
    while True:
        new_line = file.readline()
        if new_line in ["", "\n"]:
            match is_lock:
                case True: locks.append(pattern)
                case False: keys.append(pattern)
            if new_line == "":
                break
            pattern = [0] * 5
            is_lock = file.readline() == "#####\n"
            continue
        for i in range(5):
            pattern[i] += 1 if (new_line[i] == "#") else 0
for pat_l in locks:
    for pat_k in keys:
        if max([x + y for x, y in zip(pat_l, pat_k)]) < 7:
            fit += 1

print(fit)