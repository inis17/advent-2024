import re
import sys
sys.setrecursionlimit(15000)
W, H = 71, 71
firstBlock = 1024


def upPos(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])


def getAt(grid, pos):
    return grid[pos[0]][pos[1]]


def setAt(elem, grid, pos):
    grid[pos[0]][pos[1]] = elem


def flood(grid, pos, score, end, char):
    result = False
    if getAt(grid, pos) == '#' or getAt(grid, pos) == char:
        return False
    if pos == end:
        setAt(char, grid, pos)
        return True
    directions = [(0, -1),  (0, 1),  (-1, 0), (1, 0)]
    setAt(char, grid, pos)
    for d in directions:
        a = flood(grid, upPos(pos, d), score+1, end, char)
        if a:
            return a
    return False


file = open('input.txt')
result = 0
block = []
grid = [0] * (H + 2)
grid[0] = (W+2) * ['#']
for i in range(0, H):
    grid[i+1] = ['#'] + W*['.'] + ['#']
grid[H+1] = (W+2) * ['#']
p = 0
for line in file:

    i, j = [int(a) for a in re.findall('\d+', line)]
    block.append((i, j))
    if (p < firstBlock):
        grid[i+1][j+1] = '#'
    p += 1

p = firstBlock
flo = True
while flo:
    print(chr(p % 100+1000))
    setAt('#', grid, (block[p][0] + 1, block[p][1] + 1))
    flo = flood(grid, (1, 1), 0, (H, W), chr(p % 100+1000))
    print(flo, block[p], p)
    for row in grid:
        a = ''
        for char in row:
            if char == '#' or char == chr(p % 100+1000):
                a += char
            else:
                a += '.'
        print(a)
    p += 1
