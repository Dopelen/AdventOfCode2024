import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 12.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

with (open(file_path, "r", encoding="utf-8") as file):
    matrix = [list(line.strip()) for line in file]
    height, width = len(matrix), len(matrix[0])
    y, x = next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "^"), None)
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


    def simulate(matrix, row, col, cur_d):
        visited = set()
        while True:
            if not (0 <= row < height and 0 <= col < width):
                return False
            if (row, col, cur_d) in visited:
                return True
            visited.add((row, col, cur_d))
            next_row, next_col = row + d[cur_d][0], col + d[cur_d][1]
            if 0 <= next_row < height and 0 <= next_col < width and matrix[next_row][next_col] == "#":
                cur_d = (cur_d + 1) % 4
            else:
                row, col = next_row, next_col


    for r in range(height):
        for c in range(width):
            if matrix[r][c] == ".":
                matrix[r][c] = "#"
                if simulate(matrix, y, x, 0):
                    answer += 1
                matrix[r][c] = "."

print(answer)
