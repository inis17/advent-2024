import re


def gate(i1: int, i2: int, gate: str) -> int:
    if gate == 'OR':
        return i1 | i2
    if gate == 'AND':
        return i1 & i2
    if gate == 'XOR':
        return i1 ^ i2


file = open('inputmod.txt').read()
result = 0
states = {}
for i in range(0, 45):
    states['x'+str(i).zfill(2)] = 1
    states['y'+str(i).zfill(2)] = 0

operations = []
for line in file.strip().split('\n'):
    i1,  ope, i2, o1 = re.findall('\w+', line)
    states.setdefault(i1, None)
    states.setdefault(i2, None)
    states.setdefault(o1, None)
    operations.append([i1, i2, o1, ope])

while None in states.values():
    for o in operations:

        if states[o[0]] is None or states[o[1]] is None:
            continue
        # if (o[2].startswith('z01')):
        #     print(o)
        states[o[2]] = gate(states[o[0]], states[o[1]], o[3])
        # print(states[o[2]])

a = ['z13', 'vcv',
     'z19', 'vwp',
     'z25', 'mps',
     'vjv', 'cqm']
a.sort()
g = ",".join(a)
print(g)
##
# print("z01", states['z01'])
zs = [x for x in states if x.startswith('z')]
zs.sort(reverse=True)
ys = [x for x in states if x.startswith('y')]
ys.sort(reverse=True)
xs = [x for x in states if x.startswith('x')]
xs.sort(reverse=True)
# print("z01", states['z01'])
for i, x in enumerate(xs):
    a = 'x' + str(i).zfill(2) + ': ' + str(states['x' + str(i).zfill(2)])
    b = 'y' + str(i).zfill(2) + ': ' + str(states['y' + str(i).zfill(2)])
    c = 'z' + str(i).zfill(2) + ': ' + str(states['z' + str(i).zfill(2)])
    print(a + ' ' + b + ' = ' + c)
print('z45: ' + str(states['z45']))
z = ''.join(str(states[x]) for x in zs)
# print(len(z))
# print(zs)
# print(z)
# print(int(z, 2))
# print(operations)
print("fin du programme")
