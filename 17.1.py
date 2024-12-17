import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 33.txt"
file_path = os.path.join(desktop, file_name)
pointer = 0
answer = []


def combo(val):
    if val in [0, 1, 2, 3]:
        return val
    match val:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
    return False


with (open(file_path, "r", encoding="utf-8") as file):
    a = int(file.readline().split(":")[-1])
    b = int(file.readline().split(":")[-1])
    c = int(file.readline().split(":")[-1])
    file.readline()
    program = list(map(int, file.readline().split(":")[-1].split(",")))
    size = len(program)
    while pointer < size - 1:
        opcode = program[pointer]
        if opcode == 0:
            a = int(a / (2 ** combo(program[pointer + 1])))
        elif opcode == 1:
            b ^= program[pointer + 1]
        elif opcode == 2:
            b = combo(program[pointer + 1]) % 8
        elif opcode == 3:
            if a != 0:
                pointer = program[pointer + 1]
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            answer.append(combo(program[pointer + 1]) % 8)
        elif opcode == 6:
            b = int(a / (2 ** combo(program[pointer + 1])))
        elif opcode == 7:
            c = int(a / (2 ** combo(program[pointer + 1])))
        pointer += 2

print(a, b, c)
print(",".join(map(str, answer)))
