import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 22.txt"
file_path = os.path.join(desktop, file_name)
mapping = {}
result = 0


def blinking(val, left):
    if left == 0:
        return 1
    left -= 1
    if val == "0":
        fractions = mapping.get(("1", left)) or blinking("1", left)
    elif len(val) % 2 == 0:
        mid = len(val) // 2
        left_part = val[:mid]
        right_part = val[mid:].lstrip("0") or "0"
        fractions = (
                            mapping.get((left_part, left)) or blinking(left_part, left)
                    ) + (
                            mapping.get((right_part, left)) or blinking(right_part, left)
                    )
    else:
        multiplied_val = str(int(val) * 2024)
        fractions = mapping.get((multiplied_val, left)) or blinking(multiplied_val, left)

    mapping[(val, left + 1)] = fractions
    return fractions


with (open(file_path, "r", encoding="utf-8") as file):
    line = list(file.read().split())
    for elem in line:
        result += blinking(elem, 75)

print(result)
