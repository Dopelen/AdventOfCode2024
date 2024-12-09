import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 11.txt"
file_path = os.path.join(desktop, file_name)
answer = 1

with open(file_path, "r", encoding="utf-8") as file:
    matrix = [list(line.strip()) for line in file]
    height, width = len(matrix), len(matrix[0])
    y, x = next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "^"), None)
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_d = 0
    matrix[y][x] = "X"
    while True:
        new_y = y + d[cur_d][0]
        new_x = x + d[cur_d][1]
        if not (0 <= new_y < height and 0 <= new_x < width):
            break
        cur_cell = matrix[new_y][new_x]
        if cur_cell == "#":
            cur_d = (cur_d + 1) % 4
        else:
            y, x = new_y, new_x
            if cur_cell == ".":
                answer += 1
                matrix[y][x] = "X"
print(answer)
