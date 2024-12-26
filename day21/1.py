from collections import defaultdict
from itertools import permutations
file = open('example.txt')
result = 0
keypad = [['7', '8', '9'],
          ['4', '5', '6'],
          ['1', '2', '3'],
          ['#', '0', 'A']]
keys = '0123456789A'
arrowPad = [['#', '^', 'A'],
            ['<', 'v', '>']]
arrows = '<>v^A'


def findPos(item, grid):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if item == char:
                return (i, j)
    return (-1, -1)


def checkValid(start, comb, grid):
    i = start[0]
    j = start[1]
    for c in comb:
        if c == 'v':
            i += 1
        if c == '^':
            i -= 1
        if c == '>':
            j += 1
        if c == '<':
            j -= 1
        if grid[i][j] == '#':
            print('non valid:', start, comb)
            return False
    return True


def createKeyPadMap():
    padMap = defaultdict(list)
    perms = list(permutations(keys, 2))
    for p in perms:
        start = findPos(p[0], keypad)
        end = findPos(p[1], keypad)
        di = end[0] - start[0]
        dj = end[1] - start[1]

        vi = '^'
        if di > 0:
            vi = 'v'
        vj = '<'
        if dj > 0:
            vj = '>'
        combinations = set(permutations(vi*abs(di)+vj*abs(dj)))
        combinations = {
            c for c in combinations if checkValid(start, c, keypad)}
    print(p)


createKeyPadMap()
a = 3


for line in file:
    pass
