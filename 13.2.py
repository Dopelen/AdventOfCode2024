from sympy import symbols, Eq, solve
import math
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 26.txt"
file_path = os.path.join(desktop, file_name)
answer = 0


def calculate_result(data):
    cur_min = math.inf
    a, b, result = data
    x, y = symbols('x y')
    eq1 = Eq(a[0] * x + b[0] * y, result[0])
    eq2 = Eq(a[1] * x + b[1] * y, result[1])
    solution = solve((eq1, eq2), (x, y), force=True)
    if not solution:
        return 0
    if isinstance(solution, dict):
        solution = [solution]
    for sol in solution:
        pairs = (sol[x], sol[y])
        if all((el == int(el) and el > 0) for el in pairs):
            cur_min = min(cur_min, pairs[0].numerator * 3 + pairs[1].numerator)

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
             tuple([int(lines[2 + shift].split("X=")[1].split()[0][:-1]) + 10000000000000,
                    int(lines[2 + shift].split("Y=")[1].split()[0]) + 10000000000000])])
        shift += 4

    for i in range(0, len(machines), 3):
        answer += calculate_result(machines[i:i + 3])

print(answer)
