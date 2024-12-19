import os
from functools import cache

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 37.txt"
file_path = os.path.join(desktop, file_name)
answer = 0


@cache
def check_design(design: str) -> bool:
    hit = False
    for elem in patterns:
        if hit: break
        if design.startswith(elem):
            if design == elem:
                return True
            border = len(elem)
            if len(design) >= border:
                hit = check_design(design[border:])
    return hit


with (open(file_path, "r", encoding="utf-8") as file):
    patterns, designs = map(str.strip, file.read().split('\n', 1))
    patterns = patterns.replace(" ", "").split(",")
    designs = designs.splitlines()
    for elem in designs:
        answer += check_design(elem)

print(answer)
