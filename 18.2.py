import copy
import os
from collections import deque

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 36.txt"
file_path = os.path.join(desktop, file_name)
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
coords = []
size = 71

with (open(file_path, "r", encoding="utf-8") as file):
    data = file.read().split('\n')
    for elem in data:
        x, y = elem.split((","))
        coords.append((int(y), int(x)))
    matrix = [[False for c in range(size)] for r in range(size)]
    prev = None

    for y, x in coords:
        matrix[y][x] = "#"
        visited = [[False for c in range(size)] for r in range(size)]
        queue = deque([(0, 0)])
        prev = (y, x)
        if prev == (0, 0):
            break
        while queue:
            y, x = queue.popleft()
            if visited[y][x] == False:
                visited[y][x] = True
                if y == x == (size - 1):
                    break
                for dy, dx in d:
                    ny, nx = y + dy, x + dx
                    if (0 <= nx < size) and (0 <= ny < size) and matrix[ny][nx] != "#" and (visited[ny][nx] == False):
                        queue.append((ny, nx))
        if visited[size - 1][size - 1] == False:
            break
    print(prev)
