import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 40.txt"
file_path = os.path.join(desktop, file_name)
matrix = []
answer = 0
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
profits = defaultdict(int)


def find_point(char):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == char:
                return (i, j)


with (open(file_path, "r", encoding="utf-8") as file):
    new_line = file.readline().strip()
    while new_line:
        matrix.append([elem for elem in new_line])
        new_line = file.readline().strip()
    rows, cols = len(matrix), len(matrix[0])
    start = find_point("S")
    end = find_point("E")


    def pathfinder(y: int, x: int, cost: int) -> None:
        matrix[y][x] = [cost]
        while (y, x) != end:
            cost += 1
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if matrix[ny][nx] in [".", "E"]:
                    matrix[y][x].append((ny, nx))
                    matrix[ny][nx] = [cost]
                    y, x = ny, nx
                    break


    def calculate_chunk(y_cur, x_cur):
        for r in range(max(0, y_cur - 20), min(rows, y_cur + 21)):
            max_offset = 20 - abs(y_cur - r)
            for c in range(max(0, x_cur - max_offset), min(cols, x_cur + max_offset + 1)):
                if isinstance(matrix[r][c], list):
                    if matrix[y_cur][x_cur][0] + (abs(y_cur - r) + abs(x_cur - c)) < matrix[r][c][0]:
                        profits[matrix[r][c][0] - (matrix[y_cur][x_cur][0] + (abs(y_cur - r) + abs(x_cur - c)))] += 1


pathfinder(start[0], start[1], 0)
y, x = start
while True:
    if len(matrix[y][x]) == 1:
        break
    calculate_chunk(y, x)
    y, x = matrix[y][x][1]

for key, val in profits.items():
    if key >= 100:
        answer += val

print(answer)
