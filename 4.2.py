import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 8.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
d = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

def construct_xmas(r, c, first=False):
    if not (0 <= r < height and 0 <= c < width):
        return
    if first:
        first_diagonal = {construct_xmas(r + d[0][0], c + d[0][1]), construct_xmas(r + d[1][0], c + d[1][1])} == {"M", "S"}
        second_diagonal = {construct_xmas(r + d[2][0], c + d[2][1]), construct_xmas(r + d[3][0], c + d[3][1])} == {"M", "S"}
        return first_diagonal and second_diagonal
    elif matrix[r][c] in ["M", "S"]:
        return matrix[r][c]
    return 0


with (open(file_path, "r", encoding="utf-8") as file):
    matrix = [list(line.strip()) for line in file]
    height, width = len(matrix), len(matrix[0])
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == "A":
                answer += construct_xmas(row, col, True)

print(answer)