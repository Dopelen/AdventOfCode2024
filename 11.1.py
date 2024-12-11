import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 21.txt"
file_path = os.path.join(desktop, file_name)
result = 0


def blinking(val, left):
    if left == 0:
        return 1
    left -= 1
    if val == "0":
        fractions = blinking("1", left)
    elif not (len(val) % 2):
        fractions = blinking(val[:len(val) // 2], left) + blinking(val[len(val) // 2::].lstrip("0") or "0", left)
    else:
        fractions = blinking(str(int(val) * 2024), left)
    return fractions


with (open(file_path, "r", encoding="utf-8") as file):
    line = list(file.read().split())
    for elem in line:
        result += blinking(elem, 25)

print(result)
