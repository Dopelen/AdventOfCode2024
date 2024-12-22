import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 43.txt"
file_path = os.path.join(desktop, file_name)
answer = 0


def process(n: int) -> int:
    for step in range(2000):
        mult = n * 64
        n = (mix(n, mult) % 16777216)
        divid = int(n / 32)
        n = (mix(n, divid) % 16777216)
        third = n * 2048
        n = (mix(n, third) % 16777216)
    return n


def mix(v: int, mu: int) -> int:
    return v ^ mu


with open(file_path, "r", encoding="utf-8") as file:
    sec_nums = list(map(int, list(file)))
    for num in sec_nums:
        answer += process(num)

print(answer)
