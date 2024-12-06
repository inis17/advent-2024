import re
from collections import defaultdict
file = open('input.txt')
result = 0
rules = defaultdict(list)
for line in file:
    if '|' in line:
        n, p = re.findall('\d+', line)
        rules[int(n)].append(int(p))
        continue
    if (len(line) <= 1):
        continue
    update = list(map(int, line.strip().split(',')))
    isValid = True
    for idx, elem in enumerate(update):
        rule = rules[elem]
        for n in range(0, idx):
            if update[n] in rule:
                isValid = False
                break
    if isValid:
        mid = int(len(update)/2)
        result += update[mid]

print(result)
