import re


def gate(i1: int, i2: int, gate: str) -> int:
    if gate == 'OR':
        return i1 | i2
    if gate == 'AND':
        return i1 & i2
    if gate == 'XOR':
        return i1 ^ i2


file = open('input.txt').read()
result = 0
states, gates = file.split('\n\n')
states = {line.split(': ')[0]: int(line.split(': ')[1])
          for line in states.split('\n')}
operations = []
for line in gates.strip().split('\n'):
    i1,  ope, i2, o1 = re.findall('\w+', line)
    states.setdefault(i1, None)
    states.setdefault(i2, None)
    states.setdefault(o1, None)
    operations.append([i1, i2, o1, ope])

while None in states.values():
    for o in operations:

        if states[o[0]] is None or states[o[1]] is None:
            continue
        states[o[2]] = gate(states[o[0]], states[o[1]], o[3])

zs = [x for x in states if x.startswith('z')]
zs.sort(reverse=True)
z = ''.join(str(states[x]) for x in zs)


print(z)
print(int(z, 2))
# print(operations)
print("fin du programme")
