import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 29.txt"
file_path = os.path.join(desktop, file_name)
gps = 0
matrix = []
d = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}


def check_mov(cur_y, cur_x, dest):
    dy, dx = dest
    new_y, new_x = cur_y + dy, cur_x + dx
    next_el = matrix[new_y][new_x]
    if next_el == "#":
        return cur_y, cur_x
    elif next_el == ".":
        matrix[cur_y][cur_x], matrix[new_y][new_x] = matrix[new_y][new_x], matrix[cur_y][cur_x]
        return new_y, new_x
    else:
        while matrix[new_y][new_x] not in [".", "#"]:
            new_y += dy
            new_x += dx
        if matrix[new_y][new_x] == "#":
            return cur_y, cur_x
        else:
            matrix[cur_y + dy][cur_x + dx], matrix[cur_y][cur_x] = matrix[cur_y][cur_x], matrix[cur_y + dy][cur_x + dx]
            matrix[cur_y][cur_x], matrix[new_y][new_x] = matrix[new_y][new_x], matrix[cur_y][cur_x]
            return cur_y + dy, cur_x + dx


with (open(file_path, "r", encoding="utf-8") as file):
    new_line = file.readline().strip()
    while new_line:
        matrix.append([elem for elem in new_line])
        new_line = file.readline().strip()

    y, x = list(next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "@"), None))
    commands = file.read().replace('\n', "")
    for com in commands:
        y, x = check_mov(y, x, d[com])

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            gps += (100 * r + c) if (matrix[r][c] == "O") else 0

print(gps)
