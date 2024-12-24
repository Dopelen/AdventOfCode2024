import os
from collections import defaultdict, deque

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 47.txt"
file_path = os.path.join(desktop, file_name)
wires = defaultdict(int)
processed = deque()

with open(file_path, "r", encoding="utf-8") as file:
    new_line = file.readline()
    while new_line != "\n":
        wire, value = new_line.split(":")
        wires[wire] = int(value)
        new_line = file.readline()

    for command in list(file):
        operation, output = command.split("->")
        operation = operation.split()
        output = output.strip()
        processed.append(tuple(operation + [output]))

    while processed:
        cur_check = in_1, operation, in_2, out = processed.popleft()
        if in_1 in wires and in_2 in wires:
            match operation:
                case "AND": result = wires[in_1] & wires[in_2]
                case "OR": result = wires[in_1] | wires[in_2]
                case "XOR": result = wires[in_1] ^ wires[in_2]
            wires[out] = result
        else:
            processed.append(cur_check)

    z_wires = sorted([w for w in wires.keys() if w.startswith("z")], reverse=True)
print(int(''.join([str(int(wires[z])) for z in z_wires]), 2))


