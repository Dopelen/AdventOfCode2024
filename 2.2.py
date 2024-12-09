import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 4.txt"
file_path = os.path.join(desktop, file_name)
safe_counter = 0


def is_increasing(s: list[int]) -> bool:
    if all(1 <= s[i + 1] - s[i] <= 3 for i in range(len(s) - 1)):
        return True
    return False


def is_decreasing(s: list[int]) -> bool:
    if all(1 <= s[i] - s[i + 1] <= 3 for i in range(len(s) - 1)):
        return True
    return False


with (open(file_path, "r", encoding="utf-8") as file):
    for line in file:
        sequence = list(map(int, line.split()))
        for i in range(len(sequence)):
            new_string = sequence[:i] + sequence[i + 1:]
            if any([is_increasing(new_string), is_decreasing(new_string)]):
                safe_counter += 1
                break

print(safe_counter)
