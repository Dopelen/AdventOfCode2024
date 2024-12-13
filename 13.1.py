import math
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 25.txt"
file_path = os.path.join(desktop, file_name)
answer = 0


def calculate_result(data):
    a, b, result = data
    combinations = [[(i * a[0] + j * b[0], i * a[1] + j * b[1]), (i, j)] for i in range(101) for j in range(101)]
    targets = [elem[-1] for elem in combinations if elem[0] == data[-1]]
    cur_min = math.inf
    for pair in targets:
        cur_min = min(cur_min, pair[0] * 3 + pair[1])
    return cur_min if cur_min != math.inf else 0


with (open(file_path, "r", encoding="utf-8") as file):
    lines = list(file)
    machines = []
    shift = 0
    while shift < len(lines):
        machines.extend(
            [tuple(map(int, (lines[shift].split("X+")[1].split()[0][:-1], lines[shift].split("Y+")[1].split()[0]))),
             tuple(map(int,
                       (lines[1 + shift].split("X+")[1].split()[0][:-1], lines[1 + shift].split("Y+")[1].split()[0]))),
             tuple(map(int,
                       (lines[2 + shift].split("X=")[1].split()[0][:-1], lines[2 + shift].split("Y=")[1].split()[0])))])
        shift += 4

    for i in range(0, len(machines), 3):
        answer += calculate_result(machines[i:i + 3])

print(answer)
