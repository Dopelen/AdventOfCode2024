import copy
import os
from PIL import Image
import numpy as np

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 28.txt"
file_path = os.path.join(desktop, file_name)
width, height = 101, 103
iterations = 10000
robots = []
matrix = [[0] * width for _ in range(height)]
clear_matrix = copy.deepcopy(matrix)

with (open(file_path, "r", encoding="utf-8") as file):
    for line in file:
        cur_pos, velocities = line.split()
        robots.append(list(map(int, cur_pos[2:].split(",") + velocities[2:].split(","))))

    for seconds in range(1, iterations):
        matrix = copy.deepcopy(clear_matrix)
        for index, (x, y, dx, dy) in enumerate(robots):
            x = (x + dx * seconds) % width
            y = (y + dy * seconds) % height
            matrix[y][x] = 255

        array = np.array(matrix, dtype=np.uint8)
        image = Image.fromarray(array)
        image.save(f"C:\\Users\\Олег\\Desktop\\advent_of_code\\advent_of_code\\pictures\\matrix{seconds}.png")
