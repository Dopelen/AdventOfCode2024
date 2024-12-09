import os
from collections import deque

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 14.txt"
file_path = os.path.join(desktop, file_name)
answer = 0


def calculate_step(l):
    variants, new_variants = deque([l[0]]), []
    for elem in l[1:]:
        while variants:
            var = variants.popleft()
            potential_sum = var + elem
            potential_mul = var * elem
            potential_concat = int(str(var) + str(elem))
            if potential_sum <= result:
                new_variants.append(potential_sum)
            if potential_mul <= result:
                new_variants.append(potential_mul)
            if potential_concat <= result:
                new_variants.append(potential_concat)
        variants, new_variants = deque(new_variants), []
    return result in variants


with (open(file_path, "r", encoding="utf-8") as file):
    for line in file:
        result, values = line.split(":")
        result, values = int(result), list(map(int, values.split()))
        answer += result if calculate_step(values) else 0

print(answer)
