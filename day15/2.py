def upPos(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])


def getAt(grid, pos):
    return grid[pos[0]][pos[1]]


def setAt(elem, grid, pos):
    grid[pos[0]][pos[1]] = elem


def move(pos, dir, grid):
    if dir[0] == 0:
        return moveSideWay(pos, dir, grid)
    return moveVerticaly(pos, dir, grid)


def moveSideWay(pos, dir, grid):
    movingPositions = []
    nPos = upPos(pos, dir)
    if getAt(grid, nPos) == '#':
        return movingPositions
    if getAt(grid, nPos) == '.':
        movingPositions.append(pos)
        return movingPositions
    movingPositions += moveSideWay(nPos, dir, grid)
    if len(movingPositions) != 0:
        movingPositions += [pos]
    return movingPositions


def moveVerticaly(pos, dir, grid):
    movingPositions = []
    movingPositions1 = []
    movingPositions2 = []
    nPos1 = upPos(pos, dir)
    if getAt(grid, nPos1) == '#':
        return movingPositions
    if getAt(grid, nPos1) == '.':
        movingPositions.append(pos)
        return movingPositions
    if getAt(grid, nPos1) == '[':
        movingPositions1 += moveVerticaly(nPos1, dir, grid)
        movingPositions2 += moveVerticaly(upPos(nPos1, (0, 1)), dir, grid)
        if len(movingPositions1) != 0 and len(movingPositions2) != 0:
            movingPositions += [pos] + movingPositions1 + movingPositions2
        return movingPositions
    if getAt(grid, nPos1) == ']':
        movingPositions1 += moveVerticaly(nPos1, dir, grid)
        movingPositions2 += moveVerticaly(upPos(nPos1, (0, -1)), dir, grid)
        if len(movingPositions1) != 0 and len(movingPositions2) != 0:
            movingPositions += [pos] + movingPositions1 + movingPositions2
        return movingPositions


file = open('example.txt')
result = 0
grid = []
orders = ''
isGrid = True
for line in file:
    if len(line) < 2:
        isGrid = False
        continue

    if isGrid:
        row = []
        for char in line.strip():
            if char == 'O':
                row += '[]'
                continue
            if char == '@':
                row += '@.'
                continue
            row += char+char
        grid.append(row)
        continue
    orders += line.strip()

robot = (0, 0)
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == '@':
            robot = (i, j)
direction_map = {
    '<': (0, -1),  # Left
    '>': (0, 1),   # Right
    '^': (-1, 0),  # Up
    'v': (1, 0)    # Down
}
for o in orders:
    dir = direction_map[o]
    positions = move(robot, dir, grid)
    for pos in positions:
        setAt(getAt(grid, pos), grid, upPos(pos, dir))
    if len(pos) > 0:
        setAt('.', grid, robot)
        robot = upPos(robot, dir)

    for i, row in enumerate(grid):
        a = ''
        for j, char in enumerate(row):
            a += char
            if char == '[':
                result += i*100 + j
        print(a)
    input("Press Enter to continue...")

print(result)
