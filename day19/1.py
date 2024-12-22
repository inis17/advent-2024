from functools import cache
file = open('input.txt').read()
patterns, towels = file.split('\n\n')
patterns = patterns.split(', ')
towels = towels.rstrip().split('\n')

# print(patterns)
# print(towels)


@cache
def countCombinaison(t: str):
    count = 0
    if len(t) == 0:
        return 1
    for p in patterns:
        if t.startswith(p):
            count += countCombinaison(t[len(p):])
    return count


result = 0
for t in towels:
    result += countCombinaison(t)
print(result)
