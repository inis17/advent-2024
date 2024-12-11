from collections import Counter


file = open('input.txt')
result = 0
count = {}
for line in file:
    count = Counter([int(x) for x in line.split()])

for i in range(0, 75):
    nextCount = Counter()
    for key, value in count.items():
        if key == 0:
            nextCount[1] += value
            continue
        st = str(key)
        if len(st) % 2 == 0:
            n = int(len(st)/2)
            nextCount[int(st[0:n])] += value
            nextCount[int(st[-n::])] += value
            continue
        nextCount[key*2024] = value
    count = nextCount

result = sum([value for value in count.values()])


print(result)
