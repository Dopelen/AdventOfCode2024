import copy
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 34.txt"
file_path = os.path.join(desktop, file_name)

with (open(file_path, "r", encoding="utf-8") as file):
    a = int(file.readline().split(":")[-1])
    b = int(file.readline().split(":")[-1])
    c = int(file.readline().split(":")[-1])
    file.readline()
    program = list(map(int, file.readline().split(":")[-1].split(",")))


    def eval(a, b, c, i=0, R=[]):
        while i in range(len(program)):
            C = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}
            match program[i:i + 2]:
                case 0, op:
                    a = a >> C[op]
                case 1, op:
                    b = b ^ op
                case 2, op:
                    b = 7 & C[op]
                case 3, op:
                    i = op - 2 if a else i
                case 4, op:
                    b = b ^ c
                case 5, op:
                    R = R + [C[op] & 7]
                case 6, op:
                    b = a >> C[op]
                case 7, op:
                    c = a >> C[op]
            i += 2
        return R


    def find(a, i):
        if eval(a, b, c) == program:
            print(a)
        if eval(a, b, c) == program[-i:] or not i:
            for n in range(8):
                find(8 * a + n, i + 1)


    find(0, 0)
