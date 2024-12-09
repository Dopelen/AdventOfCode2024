import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 15.txt"
file_path = os.path.join(desktop, file_name)
antennas = defaultdict(list)
unic_nodes = set()


def check_antinodes(cur_t, y, x):
    for elem in antennas[cur_t]:
        dif = (y - elem[0], x - elem[1])
        first_side = (y + dif[0], x + dif[1])
        second_side = (elem[0] - dif[0], elem[1] - dif[1])
        if all([0 <= first_side[0] < height, 0 <= first_side[1] < width]):
            unic_nodes.add(first_side)
        if all([0 <= second_side[0] < height, 0 <= second_side[1] < width]):
            unic_nodes.add(second_side)


with (open(file_path, "r", encoding="utf-8") as file):
    matrix = [list(line.strip()) for line in file]
    height, width = len(matrix), len(matrix[0])
    for row in range(height):
        for col in range(width):
            current_type = matrix[row][col]
            if current_type != ".":
                check_antinodes(current_type, row, col)
                antennas[current_type].append((row, col))

print(len(unic_nodes))
