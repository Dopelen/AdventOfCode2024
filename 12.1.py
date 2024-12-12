import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 23.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()


def calculate_area(r, c, val, ar=0, per=0):
    if (not (0 <= r < width and 0 <= c < height)) or matrix[r][c] != val:
        return [0, 1]
    visited.add((r, c))
    ar += 1
    for dy, dx in directions:
        if (r + dy, c + dx) not in visited:
            recursive_call = calculate_area(r + dy, c + dx, val)
            per += recursive_call[1]
            ar += recursive_call[0]
    return [ar, per]


with (open(file_path, "r", encoding="utf-8") as file):
    matrix = [list(line.strip()) for line in file]
    height, width = len(matrix), len(matrix[0])
    for row in range(height):
        for col in range(width):
            if matrix[row][col]:
                area, perim = calculate_area(row, col, matrix[row][col])
                answer += area * perim
                for ro, co in visited:
                    matrix[ro][co] = None
                visited = set()
print(answer)
