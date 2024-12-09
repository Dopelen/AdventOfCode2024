import os, re

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 6.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

# # Solution 1
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, open(file_path).read())
do_it = True
for match in matches:
    if match == "do()":
        do_it = True
    elif match == "don't()":
        do_it = False
    else:
        if do_it:
            x, y = map(int, match[4:-1].split(","))
            answer += x * y
print(answer)