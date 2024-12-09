import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 10.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
must_be_before, must_be_after = defaultdict(set), defaultdict(set)


def travers():
    for index in range(len(page)):
        for left in range(0, index):
            if not check(index, left, must_be_after):
                return False
        for right in range(index, len(page)):
            if not check(index, right, must_be_before):
                return False
    return True


def check(index, i, d):
    if page[i] in d[page[index]]:
        page[i], page[index] = page[index], page[i]
        return False
    return True


with (open(file_path, "r", encoding="utf-8") as file):
    new_line = file.readline()
    while new_line != "\n":
        before, after = map(int, new_line.split("|"))
        must_be_before[after].add(before)
        must_be_after[before].add(after)
        new_line = file.readline()

    for line in file:
        page = list(map(int, line.split(",")))
        was_invalid = False

        if not travers():
            was_invalid = True
            while not travers():
                ...

        if was_invalid:
            answer += page[len(page) // 2]

print(answer)
