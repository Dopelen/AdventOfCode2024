import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 7.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
word = ["X", "M", "A", "S"]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def construct_xmas(coord, index, d=False):
    if not (0 <= coord[0] < height and 0 <= coord[1] < width) or matrix[coord[0]][coord[1]] != word[index]:
        return 0
    if index == 3:
        return 1
    if not d:
        return sum(construct_xmas((coord[0] + dy, coord[1] + dx), index + 1, (dy, dx)) for dy, dx in directions)
    return construct_xmas((coord[0] + d[0], coord[1] + d[1]), index + 1, d)


with (open(file_path, "r", encoding="utf-8") as file):
    matrix = [list(line.strip()) for line in file]
    height, width = len(matrix), len(matrix[0])
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == "X":
                answer += construct_xmas((row, col), 0)

print(answer)

# Before refactoring
# def construct_xmas(coord, index, direction = None):
#     if any([coord[0] < 0, coord[1] < 0, coord[0] > height - 1, coord[1] > width - 1]):
#         return 0
#     if index == 3 and matrix[coord[0]][coord[1]] == word[index]:
#         return 1
#     if not index:
#         xmas = 0
#         for dy, dx in directions:
#             xmas += construct_xmas((coord[0] + dy, coord[1] + dx), index + 1, (dy, dx))
#     else:
#         return construct_xmas((coord[0] + direction[0], coord[1] + direction[1]), index + 1, direction) if matrix[coord[0]][coord[1]] == word[index] else 0
#     return xmas
