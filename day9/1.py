file = open('input.txt')
storage = []
blank = []
for line in file:
    id = 0
    for i, c in enumerate(line.strip()):
        if i % 2 == 0:  # is even
            storage += [id] * int(c)
            id += 1
        if i % 2 == 1:
            blank.append([len(storage), int(c)])
            storage += [-1] * int(c)
blk_index = 0
curs = 0
print(str(storage))
for idx in range(len(storage) - 1, -1, -1):
    if idx == curs:
        break
    elem = storage[idx]
    if elem == -1:
        continue

    while storage[curs] != -1:
        curs += 1

    storage[curs] = elem
    storage[idx] = -1

print(str(storage))

result = [value * index for index, value in enumerate(storage) if value >= 0]
print(sum(result))
