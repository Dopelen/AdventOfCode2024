import heapq
import math
import os
from heapq import heappush

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 31.txt"
file_path = os.path.join(desktop, file_name)
matrix = []
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

with (open(file_path, "r", encoding="utf-8") as file):
    new_line = file.readline().strip()
    while new_line:
        matrix.append([elem for elem in new_line])
        new_line = file.readline().strip()

    rows, cols = len(matrix), len(matrix[0])
    start = tuple(next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "S"), None))
    end = tuple(next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "E"), None))
    distances = [[([math.inf] * 4) if matrix[r][c] != "#" else "#" for c in range(cols)] for r in range(rows)]
    p_queue = []

    initial_direction = 2
    distances[start[0]][start[1]][initial_direction] = 0
    heappush(p_queue, (0, start[0], start[1], initial_direction))

    while p_queue:
        cost, y, x, direction = heapq.heappop(p_queue)
        if cost > distances[y][x][direction]:
            continue

        if (y, x) == (end[0], end[1]):
            print(min(distances[end[0]][end[1]]))

        for i, (dy, dx) in enumerate(d):
            ny, nx = y + dy, x + dx
            if matrix[ny][nx] != "#":
                new_cost = cost + 1
                if i != direction:
                    new_cost += 1000
                if new_cost < distances[ny][nx][i]:
                    distances[ny][nx][i] = new_cost
                    heapq.heappush(p_queue, (new_cost, ny, nx, i))
