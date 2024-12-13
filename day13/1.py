import re


def calc(mach):
    ax, ay = mach['A']
    bx, by = mach['B']
    x, y = mach['Prize']
    return (x*by-y*bx)/(ax*by-ay*bx), (x*ay-y*ax)/(bx*ay-by*ax)


file = open('input.txt')
result = 0
machines = []
mach = {}
for line in file:
    if line == '\n':
        continue
    x, y = [int(x) for x in re.findall('\d+', line)]
    if "Button A:" in line:
        mach['A'] = [x, y]
    if "Button B:" in line:
        mach['B'] = [x, y]
    if "Prize:" in line:
        mach['Prize'] = [x+10000000000000, y+10000000000000]
        machines.append(mach)
        mach = {}
# print(machines)
for mach in machines:
    a, b = calc(mach)
    if a.is_integer() and b.is_integer():
        result += int(a*3+b)
print(result)
