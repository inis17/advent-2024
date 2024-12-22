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


def prgm(a, prog):
    b = 0
    c = 0
    out = ""
    ptr = 0
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
    return out


file = open('input.txt')
a, B, B = 0, 0, 0
p = []
for line in file:
    if 'P' in line:
        p = [int(a) for a in re.findall('\d+', line)]
        continue

prog = ''.join([str(x)for x in p])


lst = {x: prgm(x, prog) for x in range(8)}
# print(lst)
res = [10794, 1, 5, 6, 727, 1, 1, 6, 5]
res = [10794, 0, 6, 5, 727, 0, 0, 6, 5]
i = 0

while prog != prgm(a, prog):

    print('i :', i)
    res = [i, 0, 6, 5, 727, 0, 0, 6, 5]
    offset = 0
    a = 0
    for elem in res:

        r = prgm(elem, prog)
        # print(elem, offset, r)
        a += (int(elem) << 3*offset)
        offset += len(r)

    # print(a)
    i += 1
print(a)
print(str(prgm(a, prog)).rjust(20, ' '))
print(prog.rjust(20, ' '))
