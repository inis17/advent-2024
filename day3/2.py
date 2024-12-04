import re
import math
file = open('input.txt')
result = 0
enabled = True
for line in file:
    muls = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", line)
    for elem in muls:
        if elem == "do()":
            enabled = True
            continue
        if elem == "don't()":
            enabled = False
            continue
        if enabled:
            result = result + math.prod([int(num)
                                         for num in re.findall("\d+", elem)])
print(result)
