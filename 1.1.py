import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
first, second = [], []
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        left, right = map(int, line.split())
        first.append(left)
        second.append(right)
first.sort()
second.sort()
for min_left, min_right in zip(first, second):
    answer += abs(min_left - min_right)

print(answer)