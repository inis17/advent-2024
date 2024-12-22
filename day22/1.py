file = open('test1')
result = 0
mod = 16777215  # 2^24


def calcNext(s):
    s = (s ^ (s << 6)) & mod
    s = (s ^ (s >> 5)) & mod  # 2^5
    s = (s ^ (s << 11)) & mod  # 2^11
    return s


# s = 123
# for i in range(0, 10):
#     s = calcNext(s)
#     print(s)

for line in file:
    s = int(line.strip())
    for i in range(0, 2000):
        s = calcNext(s)
    result += (s)
    # print(s)


print(result)
