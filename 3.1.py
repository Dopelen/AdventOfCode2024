import os, re

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 5.txt"
file_path = os.path.join(desktop, file_name)
answer = 0


with (open(file_path, "r", encoding="utf-8") as file):
    for line in file:
        pattern = r'mul\(\d{1,3},\d{1,3}\)'
        matches = re.findall(pattern, line)
        processed_chunks = [list(map(int, elem[4:-1].split(","))) for elem in matches]
        answer += sum(first_num * second_num for first_num, second_num in processed_chunks)

print(answer)
