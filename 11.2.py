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
    elif not (len(val) % 2):
        fractions = (mapping.get((val[:len(val) // 2], left)) or blinking(val[:len(val) // 2], left)) + (
                mapping.get((val[len(val) // 2::].lstrip("0") or "0",
                             left)) or blinking(val[len(val) // 2::].lstrip("0") or "0",
                                                left))
    else:
        fractions = mapping.get((str(int(val) * 2024), left)) or blinking(str(int(val) * 2024), left)

    mapping[(val, left + 1)] = fractions
    return fractions


with (open(file_path, "r", encoding="utf-8") as file):
    line = list(file.read().split())
    for elem in line:
        result += blinking(elem, 75)

print(result)
