import re
import sys
sys.setrecursionlimit(15000)
W, H = 71, 71


def upPos(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])


def getAt(grid, pos):
    return grid[pos[0]][pos[1]]


def setAt(elem, grid, pos):
    grid[pos[0]][pos[1]] = elem


def flood(grid, pos, score, end):
    if getAt(grid, pos) == '#':
        return False
    if pos == end:
        setAt(score, grid, pos)
        return score
    directions = [(0, -1),  (0, 1),  (-1, 0), (1, 0)]
    if getAt(grid, pos) == '.':
        setAt(score, grid, pos)
        for d in directions:
            a = flood(grid, upPos(pos, d), score+1, end)
    if int(getAt(grid, pos)) > score:
        setAt(score, grid, pos)
        for d in directions:
            a = flood(grid, upPos(pos, d), score+1, end)
    return 0


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
    if (p < 1024):
        grid[i+1][j+1] = '#'
    p += 1

print(flood(grid, (1, 1), 0, (H, W)))
for row in grid:
    a = ''
    for char in row:
        a += str(char).center(3, ' ')
    print(a)
print(getAt(grid, (H, W)))
