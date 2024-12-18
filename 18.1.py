import heapq
import math
import os
from heapq import heappush

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 35.txt"
file_path = os.path.join(desktop, file_name)
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
coords = set()
size = 71

with (open(file_path, "r", encoding="utf-8") as file):
    data = file.read().split('\n')
    for elem in data[0:1024]:
        x, y = elem.split((","))
        coords.add((int(y), int(x)))
    matrix = [[math.inf if ((r, c) not in coords) else "#" for c in range(size)] for r in range(size)]
    p_queue = []
    matrix[0][0] = 0
    heappush(p_queue, (0, 0, 0))

    while p_queue:
        cost, y, x = heapq.heappop(p_queue)
        if cost > matrix[y][x]:
            continue
        if (y, x) == (size - 1, size - 1):
            print(matrix[size - 1][size - 1])
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if (0 <= nx < size) and (0 <= ny < size):
                if (matrix[ny][nx] != "#") and (matrix[ny][nx] > cost + 1):
                    matrix[ny][nx] = cost + 1
                    heapq.heappush(p_queue, (cost + 1, ny, nx))
