import re
import math
file = open('input.txt')
result = 0
for line in file:
    muls = re.findall("mul\(\d+,\d+\)", line)
    print(len(muls))
    for elem in muls:
        result = result + math.prod([int(num)
                                    for num in re.findall("\d+", elem)])


print(result)
