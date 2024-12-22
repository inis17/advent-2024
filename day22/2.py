from collections import Counter
file = open('input.txt')
result = 0
mod = 16777215  # 2^24


def calcNext(s):
    s = (s ^ (s << 6)) & mod
    s = (s ^ (s >> 5)) & mod  # 2^5
    s = (s ^ (s << 11)) & mod  # 2^11
    return s


tot = Counter({})
for line in file:
    s = int(line.strip())
    first = s % 10
    second = None
    third = None
    fourth = None
    d = Counter({})
    id = None
    for i in range(0, 2000):
        # if (i == 1999):
        #     print("end of loop")
        s = calcNext(s)
        zero = s % 10
        if first is not None and second is not None and third is not None and fourth is not None:
            id = str(third-fourth)+str(second-third) + \
                str(first-second)+str(zero-first)
        fourth = third
        third = second
        second = first
        first = zero
        if id is not None:
            d.setdefault(id, zero)

    tot += d

print(max(tot.values()))
