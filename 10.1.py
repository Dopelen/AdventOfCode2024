import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 19.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def construct_trail(y, x, step, dest):
    if not((0 <= y <= height - 1) and (0 <= x <= width - 1)) or matrix[y][x] != step:
        return
    if step == 9:
        dest.add((y, x))
    else:
        for dy, dx in directions:
            construct_trail(y + dy, x + dx, step + 1, dest)

with (open(file_path, "r", encoding="utf-8") as file):
    matrix = [list(map(int, line.strip())) for line in file]
    height, width = len(matrix), len(matrix[0])
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == 0:
                dest = set()
                construct_trail(row, col, 0, dest)
                answer += len(dest)

print(answer)