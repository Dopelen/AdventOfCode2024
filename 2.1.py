import os
from collections import deque

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 3.txt"
file_path = os.path.join(desktop, file_name)
safe_counter = 0

# index version
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        seq = list(map(int, line.split()))
        ind = 0
        asc = seq[ind] < seq[ind + 1]
        while ind < len(seq) - 1:
            if any([asc and seq[ind] >= seq[ind + 1],
                    not asc and seq[ind] <= seq[ind + 1],
                    abs(seq[ind] - seq[ind + 1]) not in [1, 2, 3]]):
                break
            ind += 1
        safe_counter += ind == len(seq) - 1

print(safe_counter)

# deque version
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        seq = deque(map(int, line.split()))
        first = seq.popleft()
        asc = first < seq[0]
        safe = True
        while seq:
            second = seq.popleft()
            if ((asc and first >= second) or (not asc and first <= second)) or (abs(second - first) not in [1, 2, 3]):
                safe = False
                break
            first = second
        if not seq and safe:
            safe_counter += 1