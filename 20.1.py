import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 39.txt"
file_path = os.path.join(desktop, file_name)
matrix = []
answer = 0
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
profits = defaultdict(int)

with (open(file_path, "r", encoding="utf-8") as file):
    new_line = file.readline().strip()
    while new_line:
        matrix.append([elem for elem in new_line])
        new_line = file.readline().strip()
    rows, cols = len(matrix), len(matrix[0])
    start = tuple(next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "S"), None))
    end = tuple(next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "E"), None))


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


    def cheat_move(y: int, x: int) -> None:
        matrix[end[0]][end[1]].append((end[0], end[1]))
        while (y, x) != end:
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if matrix[ny][nx] == "#":
                    for cy, cx in d:
                        vy, vx = ny + cy, nx + cx
                        if (0 <= vy < rows) and (0 <= vx < cols) and isinstance(matrix[vy][vx], list):
                            if (matrix[y][x][0] + 2) < matrix[vy][vx][0]:
                                profits[matrix[vy][vx][0] - (matrix[y][x][0] + 2)] += 1
            y, x = matrix[y][x][1]

pathfinder(start[0], start[1], 0)
total_cost = matrix[end[0]][end[1]][0]
cheat_move(start[0], start[1])
for row in matrix:
    print(row)

for key, val in profits.items():
    if key >= 100:
        answer += val
print(answer)
