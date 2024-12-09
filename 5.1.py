import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 9.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
must_be_before, must_be_after = defaultdict(set), defaultdict(set)

with (open(file_path, "r", encoding="utf-8") as file):
    new_line = file.readline()
    while new_line != "\n":
        before, after = map(int, new_line.split("|"))
        must_be_before[after].add(before)
        must_be_after[before].add(after)
        new_line = file.readline()

    for line in file:
        page = list(map(int, line.split(",")))
        valid = True
        for index in range(len(page)):
            if not valid: break
            for left in range(0, index):
                if page[left] in must_be_after[page[index]]:
                    valid = False
            for right in range(index, len(page)):
                if page[right] in must_be_before[page[index]]:
                    valid = False
        if valid:
            answer += page[len(page) // 2]

print(answer)
