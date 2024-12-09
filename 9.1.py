import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 17.txt"
file_path = os.path.join(desktop, file_name)

with (open(file_path, "r", encoding="utf-8") as file):
    line = list(map(int, file.read()))
    processed = []
    space = False
    id = 0
    for i in range(len(line)):
        value = id if not space else None
        processed.extend([value] * line[i])
        space = not space
        if space: id += 1

    point_1 = 0
    size = point_2 = len(processed)
    point_2 -= 1

    while True:
        while point_2 > -1 and processed[point_2] == None:
            point_2 -= 1
        while point_1 < size - 1 and processed[point_1] != None:
            point_1 += 1
        if point_1 >= point_2:
            break
        processed[point_1], processed[point_2] = processed[point_2], processed[point_1]
        point_2 -= 1

print(sum(elem * index for index, elem in enumerate(processed[:point_2 + 1])))

    # shift = 0
    # for i in range(len(line)):
    #     if i % 2:
    #         empty.extend([j + shift for j in range(line[i])])
    #     shift += line[i]

