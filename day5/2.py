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
    notClean = True
    while notClean:
        notClean = False
        for elem in update:
            idx = update.index(elem)
            rule = rules[elem]
            for n in range(0, idx):
                if update[n] == elem:
                    break
                if update[n] in rule:
                    isValid = False
                    moved = update[n]
                    update.insert(idx + 1, moved)
                    update.pop(n)
                    n = n-1
                    notClean = True
    if not isValid:
        print(update)
        mid = int(len(update)/2)
        result += update[mid]

print(result)
