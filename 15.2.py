import copy
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 30.txt"
file_path = os.path.join(desktop, file_name)
gps = 0
matrix = []
d = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}
multiplier = {".": [".", "."], "O": ["[", "]"], "#": ["#", "#"], "@": ["@", "."]}
box = {"[": (0, 1), "]": (0, -1)}


def shift(new_m, y, x, dest, side_call=False):
    if new_m[y][x] == "#":
        return False
    else:
        if new_m[y][x] == ".":
            return y
        else:
            up = shift(new_m, y + dest[0], x + dest[1], dest)
            if up:
                if not side_call:
                    side = shift(new_m, y, x + box[matrix[y][x]][1], dest, True)
                    if (up and side) and (up == side):
                        new_m[y][x + box[matrix[y][x]][1]], new_m[y + dest[0]][x + box[matrix[y][x]][1]] = new_m[y + dest[0]][x + box[matrix[y][x]][1]], new_m[y][x + box[matrix[y][x]][1]]
                        new_m[y][x], new_m[up][x] = new_m[up][x], new_m[y][x]
                        return up - dest[0]
                    else:
                        return False
                return up
            return False


def check_mov(cur_y, cur_x, dest):
    global matrix
    dy, dx = dest
    new_y, new_x = cur_y + dy, cur_x + dx
    next_el = matrix[new_y][new_x]
    if next_el == "#":
        return cur_y, cur_x
    elif next_el == ".":
        matrix[cur_y][cur_x], matrix[new_y][new_x] = matrix[new_y][new_x], matrix[cur_y][cur_x]
        return new_y, new_x
    else:
        if dx in [-1, 1]:
            while matrix[new_y][new_x] not in [".", "#"]:
                new_y += dy
                new_x += dx
            if matrix[new_y][new_x] == "#":
                return cur_y, cur_x
            else:
                if dx == 1:
                    matrix[cur_y] = matrix[cur_y][:cur_x] + [".", "@"] + matrix[cur_y][cur_x + 1:new_x] + matrix[cur_y][
                                                                                                          new_x + 1:]
                else:
                    matrix[cur_y] = matrix[cur_y][:new_x] + matrix[cur_y][new_x + 1:cur_x] + ["@", "."] + matrix[cur_y][
                                                                                                          cur_x + 1:]
            return cur_y + dy, cur_x + dx
        else:
            new_matrix = copy.deepcopy(matrix)
            if shift(new_matrix, cur_y + dy, cur_x + dx, dest):
                matrix = new_matrix
                matrix[cur_y][cur_x] = "."
                return cur_y + dy, cur_x + dx
            return cur_y, cur_x


with (open(file_path, "r", encoding="utf-8") as file):
    new_line = file.readline().strip()
    while new_line:
        new_row = []
        for elem in new_line:
            new_row.extend(multiplier[elem])
        matrix.append(new_row)
        new_line = file.readline().strip()
    y, x = list(next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "@"), None))
    commands = file.read().replace('\n', "")
    for com in commands:
        y, x = check_mov(y, x, d[com])

for row in matrix:
    print(row)

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        gps += (100 * r + c) if (matrix[r][c] == "[") else 0

print(gps)
