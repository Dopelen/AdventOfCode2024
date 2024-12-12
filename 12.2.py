import math
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 24.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()


def finde_all_cords(r, c, val):
    if (not (0 <= r < width and 0 <= c < height)) or matrix[r][c] != val:
        return
    visited.add((r, c))
    for dy, dx in directions:
        if (r + dy, c + dx) not in visited:
            finde_all_cords(r + dy, c + dx, val)
    return


def calculate_cost(coords):
    processed_x_left, processed_x_right, processed_y_up, processed_y_down = sorted(coords), sorted(coords), sorted(
        coords), sorted(coords)
    x_sides = y_sides = 0

    while processed_y_up:
        elem = processed_y_up.pop()
        if ((elem[0] - 1, elem[1]) not in coords):
            y_sides += 1
        if all([(elem[0] - 1, elem[1]) not in coords, (elem[0], elem[1] + 1) in coords,
                (elem[0] - 1, elem[1] + 1) not in coords]):
            y_sides -= 1

    while processed_y_down:
        elem = processed_y_down.pop()
        if ((elem[0] + 1, elem[1]) not in coords):
            y_sides += 1
        if all([(elem[0] + 1, elem[1]) not in coords, (elem[0], elem[1] + 1) in coords,
                (elem[0] + 1, elem[1] + 1) not in coords]):
            y_sides -= 1

    while processed_x_left:
        elem = processed_x_left.pop()
        if ((elem[0], elem[1] - 1) not in coords):
            x_sides += 1
        if all([(elem[0], elem[1] - 1) not in coords, (elem[0] + 1, elem[1]) in coords,
                (elem[0] + 1, elem[1] - 1) not in coords]):
            x_sides -= 1

    while processed_x_right:
        elem = processed_x_right.pop()
        if ((elem[0], elem[1] + 1) not in coords):
            x_sides += 1
        if all([(elem[0], elem[1] + 1) not in coords, (elem[0] + 1, elem[1]) in coords,
                (elem[0] + 1, elem[1] + 1) not in coords]):
            x_sides -= 1

    return x_sides + y_sides


with (open(file_path, "r", encoding="utf-8") as file):
    matrix = [list(line.strip()) for line in file]
    height, width = len(matrix), len(matrix[0])
    for row in range(height):
        for col in range(width):
            if matrix[row][col]:
                finde_all_cords(row, col, matrix[row][col])
                answer += len(visited) * calculate_cost(visited)
                for ro, co in visited:
                    matrix[ro][co] = None
                visited = set()
print(answer)
