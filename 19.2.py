import os
from collections import defaultdict
from functools import cache

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 38.txt"
file_path = os.path.join(desktop, file_name)
answer = 0


@cache
def find_combinations(target: str, patterns: tuple) -> int:
    if not target:
        return 1

    total_combinations = 0
    for pattern in patterns:
        if target.startswith(pattern):
            total_combinations += find_combinations(target[len(pattern):], patterns)
    return total_combinations


with open(file_path, "r", encoding="utf-8") as file:
    patterns, designs = map(str.strip, file.read().split('\n', 1))
    patterns = tuple(patterns.replace(" ", "").split(","))
    designs = designs.splitlines()
    for elem in designs:
        answer += find_combinations(elem, patterns)

print(answer)
