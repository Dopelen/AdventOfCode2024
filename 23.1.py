import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 45.txt"
file_path = os.path.join(desktop, file_name)
groups = defaultdict(set)
multiplayer = list()

with open(file_path, "r", encoding="utf-8") as file:
    connections = list(file)
    for connect in connections:
        first, second = connect.strip().split("-")
        groups[first].add(second)
        groups[second].add(first)

    for key, value in groups.items():
        for elem in value:
            for elem_2 in groups[elem]:
                if key in groups[elem_2] and any([key.startswith("t"), elem.startswith("t"), elem_2.startswith("t")]):
                    con = {key, elem, elem_2}
                    if con not in multiplayer:
                        multiplayer.append(con)

    multiplayer_set = [set(elem) for elem in multiplayer]
    print(len(multiplayer_set))
