import re


def combo(code, a, b, c):
    if code < 4:
        return code
    if code == 4:
        return a
    if code == 5:
        return b
    if code == 6:
        return c
    print("invalide operande :", code)


file = open('input.txt')
a, b, c = 0, 0, 0
p = []
for line in file:
    if 'A' in line:
        a = [int(a) for a in re.findall('\d+', line)][0]
        continue
    if 'B' in line:
        b = [int(a) for a in re.findall('\d+', line)][0]
        continue
    if 'C' in line:
        c = [int(a) for a in re.findall('\d+', line)][0]
        continue
    if 'P' in line:
        p = [int(a) for a in re.findall('\d+', line)]
        continue
print(a, b, c)
print(p)

ptr = 0
out = ''
while ptr < len(p):
    inst = p[ptr]
    ltr = p[ptr+1]
    cbo = combo(p[ptr + 1], a, b, c)
    # print(ope, inst)
    if inst == 0:
        a = int(a / 2**cbo)
        ptr += 2
        continue
    elif inst == 1:
        b = b ^ ltr
        ptr += 2
        continue
    elif inst == 2:
        b = cbo % 8
        ptr += 2
        continue
    elif inst == 3:
        if a == 0:
            ptr += 2
            continue
        ptr = ltr
        continue
    elif inst == 4:
        b = b ^ c
        ptr += 2
        continue
    elif inst == 5:
        out += str(cbo % 8)
        ptr += 2
        continue
    elif inst == 6:
        b = a // 2**cbo
        ptr += 2
        continue
    elif inst == 7:
        c = a // 2**cbo
        ptr += 2
        continue

print(','.join(out))
