import os
from collections import defaultdict
from functools import cache

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 44.txt"
file_path = os.path.join(desktop, file_name)
total_counter = {}


@cache
def process(n: int) -> int:
    s = [int(str(n)[-1])]
    for step in range(2000):
        mult = n * 64
        n = (mix(n, mult) % 16777216)
        divid = int(n / 32)
        n = (mix(n, divid) % 16777216)
        third = n * 2048
        n = (mix(n, third) % 16777216)
        s.append(int(str(n)[-1]))
    return s


@cache
def mix(v: int, mu: int) -> int:
    return v ^ mu


with open(file_path, "r", encoding="utf-8") as file:
    sec_nums = list(map(int, list(file)))
    for num in sec_nums:
        seq = process(num)
        local_counter = defaultdict(int)
        changes = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
        pointer = 4
        while pointer < len(seq):
            current_seq = tuple(changes[pointer - 4: pointer])
            if local_counter.get(current_seq) is None:
                local_counter[current_seq] += seq[pointer]
            pointer += 1

        for key, val in local_counter.items():
            if total_counter.get(key):
                total_counter[key] += val
            else:
                total_counter[key] = val

print(max(total_counter.values()))
