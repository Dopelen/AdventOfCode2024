import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 2.txt"
file_path = os.path.join(desktop, file_name)
first, second = defaultdict(int), defaultdict(int)
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        left, right = map(int, line.split())
        first[left] += 1
        second[right] += 1

for key in first:
    answer += key * first[key] * second[key]
print(answer)
