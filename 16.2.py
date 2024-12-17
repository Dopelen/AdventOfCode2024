import heapq
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 32.txt"
file_path = os.path.join(desktop, file_name)
matrix = []
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

with (open(file_path, "r", encoding="utf-8") as file):
    new_line = file.readline().strip()
    while new_line:
        matrix.append([elem for elem in new_line])
        new_line = file.readline().strip()
    rows, cols = len(matrix), len(matrix[0])
    start = tuple(next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "S"), None))
    end = tuple(next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == "E"), None))


    def part1():
        dist = dijkstra(matrix, [(start[0], start[1], "E")])
        best = 1000000000
        for dir in "EWNS":
            if (end[0], end[1], dir) in dist:
                best = min(best, dist[(end[0], end[1], dir)])
        return best


    def dijkstra(grid, starts):
        delta = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}

        dist = {}
        pq = []
        for sr, sc, dir in starts:
            dist[(sr, sc, dir)] = 0
            heapq.heappush(pq, (0, sr, sc, dir))

        while pq:
            (d, row, col, direction) = heapq.heappop(pq)
            if dist[(row, col, direction)] < d:
                continue
            for next_dir in "EWNS".replace(direction, ""):
                if (row, col, next_dir) not in dist or dist[
                    (row, col, next_dir)
                ] > d + 1000:
                    dist[(row, col, next_dir)] = d + 1000
                    heapq.heappush(pq, (d + 1000, row, col, next_dir))
            dr, dc = delta[direction]
            next_row, next_col = row + dr, col + dc
            if (
                    0 <= next_row < len(grid)
                    and 0 <= next_col < len(grid[0])
                    and grid[next_row][next_col] != "#"
                    and (
                    (next_row, next_col, direction) not in dist
                    or dist[(next_row, next_col, direction)] > d + 1
            )
            ):
                dist[(next_row, next_col, direction)] = d + 1
                heapq.heappush(pq, (d + 1, next_row, next_col, direction))

        return dist


    from_start = dijkstra(matrix, [(start[0], start[1], "E")])
    from_end = dijkstra(matrix, [(end[0], end[1], d) for d in "EWNS"])
    optimal = part1()
    flip = {"E": "W", "W": "E", "N": "S", "S": "N"}
    result = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for dir in "EWNS":
                state_from_start = (row, col, dir)
                state_from_end = (row, col, flip[dir])
                if state_from_start in from_start and state_from_end in from_end:
                    if (
                            from_start[state_from_start] + from_end[state_from_end]
                            == optimal
                    ):
                        result.add((row, col))
print(len(result))
