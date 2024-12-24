import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 48.txt"
file_path = os.path.join(desktop, file_name)

wires = {}
operations = []
highest_z = "z00"


def process(operation, in_1, in_2):
    match operation:
        case "AND":
            return in_1 & in_2
        case "OR":
            return in_1 | in_2
        case "XOR":
            return in_1 ^ in_2


with open(file_path, "r", encoding="utf-8") as file:
    new_line = file.readline()
    while new_line != "\n":
        wire, value = new_line.split(": ")
        wires[wire] = int(value)
        new_line = file.readline()

    for command in list(file):
        operation, output = command.split("->")
        operation = operation.split()
        output = output.strip()
        operations.append(tuple(operation + [output]))

        if output[0] == "z" and int(output[1:]) > int(highest_z[1:]):
            highest_z = output

wrong = set()
for op1, op, op2, res in operations:
    if res[0] == "z" and op != "XOR" and res != highest_z:
        wrong.add(res)
    if (
            op == "XOR"
            and res[0] not in ["x", "y", "z"]
            and op1[0] not in ["x", "y", "z"]
            and op2[0] not in ["x", "y", "z"]
    ):
        wrong.add(res)
    if op == "AND" and "x00" not in [op1, op2]:
        for subop1, subop, subop2, subres in operations:
            if (res == subop1 or res == subop2) and subop != "OR":
                wrong.add(res)
    if op == "XOR":
        for subop1, subop, subop2, subres in operations:
            if (res == subop1 or res == subop2) and subop == "OR":
                wrong.add(res)

while len(operations):
    op1, op, op2, res = operations.pop(0)
    if op1 in wires and op2 in wires:
        wires[res] = process(op, wires[op1], wires[op2])
    else:
        operations.append((op1, op, op2, res))

bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
print(int("".join(bits), 2))
print(",".join(sorted(wrong)))
