from itertools import chain
file = open('input.txt')
storage = []
for line in file:
    id = 0
    for i, c in enumerate(line.strip()):
        if i % 2 == 0:  # is even
            storage.extend([id] * int(c))
            id += 1
        if i % 2 == 1:
            storage.extend([-1] * int(c))

for i in range(len(storage)-1, -1, -1):
    eli = storage[i]
    if len(eli) < 1:
        continue
    if eli[0] == -1:
        continue
    n = len(eli)
    for j, elj in enumerate(storage):
        if j > i:
            break
        if len(elj) < n:
            continue
        if elj[0] != -1:
            continue
        storage[j] = storage[j][:-n]
        storage[i] = [-1] * len(eli)
        storage.insert(j, eli)
        break

result = sum([value * index for index,
              value in enumerate(list(chain.from_iterable(storage))) if value >= 0])
print(result)
