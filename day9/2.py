file = open('example.txt')
storage = []
blank = []
files = []
for line in file:
    id = 0
    idx = 0
    for i, c in enumerate(line.strip()):
        if i % 2 == 0:  # is even
            files.append([idx, id, int(c)])
            id += 1
            idx += int(c)
        if i % 2 == 1:
            blank.append([idx, -1, int(c)])
            idx += int(c)
curs = 0
for idx in range(len(files) - 1, -1, -1):
    end = False
    e = files[idx]
    for i, b in enumerate(blank):
        if b[0] > e[0]:
            end = True
            break
        if e[2] <= b[2]:
            b[0] += e[2]
            b[2] -= e[2]
            files.insert(i+1+curs, [i+1+curs, e[1], e[2]])
            e[1] = -1
    if end:
        continue
result = []
i = 0
j = 0
print(files)
print(blank)
while i < len(files) and j < len(blank):
    if files[i][0] < blank[j][0]:
        i += 1
        result += [files[i][1]] * files[i][2]
    if files[i][0] > blank[j][0]:
        j += 1
        result += [blank[i][1]] * blank[i][2]
print(result)
