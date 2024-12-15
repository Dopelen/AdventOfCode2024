import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 27.txt"
file_path = os.path.join(desktop, file_name)
width, height = 101, 103
iterations = 100
robots = []
matrix = [[0] * width for _ in range(height)]


def sum_square(top_left, border_y, border_x):
    row_start, col_start = top_left
    total = 0
    for i in range(row_start, border_y):
        total += sum(matrix[i][col_start:border_x])
    return total if total else 1


with (open(file_path, "r", encoding="utf-8") as file):
    for line in file:
        cur_pos, velocities = line.split()
        robots.append(tuple(map(int, cur_pos[2:].split(",") + velocities[2:].split(","))))
    for x, y, dx, dy in robots:
        x = (x + dx * iterations) % width
        y = (y + dy * iterations) % height
        matrix[y][x] += 1

    x_l, x_m, x_r = 0, width // 2, width
    y_l, y_m, y_r = 0, height // 2, height
    pairs = [((y_l, x_l), y_m, x_m),
             ((y_l, x_m + 1), y_m, x_r),
             ((y_m + 1, x_l), y_r, x_m),
             ((y_m + 1, x_m + 1), y_r, x_r)]

    answer = 1
    for args in pairs:
        answer *= sum_square(*args)

print(answer)
