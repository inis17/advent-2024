from operator import add
file = open('input.txt').read()
inputs = file.strip().split('\n\n')
result = 0
keys = []
locks = []

for elem in inputs:
    lines = elem.strip().split('\n')
    iskey = False
    if '#' not in lines[0]:
        # key
        iskey = True
    a = [-1] * 5
    for line in lines:
        for i, char in enumerate(line.strip()):
            if char == '#':
                a[i] += 1
    if iskey:
        keys.append(a)
    else:
        locks.append(a)

for k in keys:
    for l in locks:
        if max(list(map(add, k, l))) <= 5:
            result += 1

print(result)
