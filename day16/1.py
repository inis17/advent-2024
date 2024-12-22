import sys
sys.setrecursionlimit(15000)


def upPos(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])


def getAt(grid, pos):
    return grid[pos[0]][pos[1]]


def setAt(elem, grid, pos):
    grid[pos[0]][pos[1]] = elem


def printGrid(grid, pos):
    for i, row in enumerate(grid):
        a = ''
        for j, char in enumerate(row):
            if (i, j) == pos:
                a += '@'
            elif isinstance(char, int):
                a += '1'
            else:
                a += char
        print(a)


def getNextHead(pos, dir, grid, score, path, endPos):
    result = []
    directions = [(0, -1),  (0, 1),  (-1, 0), (1, 0)]
    if pos == endPos:
        return []
    for d in directions:
        nPos = upPos(pos, d)
        if nPos in path:
            continue
        if getAt(grid, nPos) == '#':
            continue
        if getAt(grid, nPos) == 'S':
            continue

        nScore = score+1
        if dir[0] == -d[0] and dir[1] == -d[1]:
            nScore += 2000
        elif dir == d:
            pass
        else:
            nScore += 1000

        if getAt(grid, nPos) == '.' or getAt(grid, nPos) == 'E':
            result.append({'score': nScore, 'dir': d,
                          'pos': nPos, 'path': path + [nPos]})
    return result


def findOnePath(pos, dir, grid, score, path, endPos):
    directions = [(0, -1),  (0, 1),  (-1, 0), (1, 0)]
    if pos == endPos:
        return score
    for d in directions:
        nPos = upPos(pos, d)
        if nPos in path:
            continue
        if getAt(grid, nPos) == '#':
            continue
        if getAt(grid, nPos) == 'S':
            continue

        nScore = score+1
        if dir[0] == -d[0] and dir[1] == -d[1]:
            nScore += 2000
        elif dir == d:
            pass
        else:
            nScore += 1000

        if getAt(grid, nPos) == '.' or getAt(grid, nPos) == 'E':
            a = findOnePath(nPos, d, grid, nScore, path + [nPos], endPos)
            if a > 0:
                return a
    return 0


def load(fileName):
    grid = []
    file = open(fileName)

    for line in file:
        grid.append([x for x in line.strip()])
    start = None
    end = None
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 'S':
                start = (i, j)
            if value == 'E':
                end = (i, j)

    return start, end, grid


start, end, grid = load('input.txt')

startDir = (0, 1)

endReach = False
maxScore = 0
completePath = []
pathHeads = [{'score': 0, 'dir': startDir, 'pos': start, 'path': [start]}]
a = findOnePath(start, startDir, grid, 0, [start], end)
print(a)
input('aaa')
while not endReach or len(pathHeads) > 0:
    newPathHeads = []
    if not endReach:
        maxScore = max([a['score'] for a in pathHeads])
    else:

        print([a['score'] for a in completePath])
        maxScore = min([a['score'] for a in completePath])
    for h in pathHeads:

        if h['pos'] == end:
            print(h)
            endReach = True
            completePath += [h]

        if not endReach:
            if maxScore >= h['score']:
                newPathHeads += getNextHead(h['pos'], h['dir'],
                                            grid, h['score'], h['path'], end)
            if maxScore < h['score']:
                newPathHeads += [h]
        elif h['score'] < maxScore:
            newPathHeads += getNextHead(h['pos'], h['dir'],
                                        grid, h['score'], h['path'], end)

    pathHeads = newPathHeads
    print(maxScore, endReach, len(pathHeads))

print(min([a['score'] for a in completePath]))
