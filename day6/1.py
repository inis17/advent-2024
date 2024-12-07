import copy
file = open('example')
result = 0
N = '^'
E = '>'
W = '<'
S = 'v'
nesw = [N, E, S, W]
binNESW = {N: 0b0001, E: 0b0010, S: 0b0100, W: 0b1000}
obstacle = '#'


def setPassed(val, dir):
    binDir = binNESW[dir]
    if val == '.':
        return binDir
    return int(val) | binDir


def hasPassed(val, dir):
    binDir = binNESW[dir]
    if val == '.':
        return False
    return int(val) & binDir != 0


grid = []
row = 0
col = 0
dir = N
for line in file:
    for elem in [N, E, W, S]:
        if elem in line:
            dir = elem
            col = line.index(elem)
            row = len(grid)
            break
    grid.append(list(line.strip()))
width = len(grid[0])
height = len(grid)
startRow = row
startCol = col
startDir = dir
grid[row][col] = '.'
possibleRowCol = []
print(row, col)

isOut = False
while not isOut:
    nextRow = row
    nextCol = col
    if dir == S:
        nextRow = row + 1
    if dir == N:
        nextRow = row - 1
    if dir == E:
        nextCol = col + 1
    if dir == W:
        nextCol = col - 1

    if height - 1 < nextRow or nextRow < 0 or width - 1 < nextCol or nextCol < 0:
        isOut = True
        break
    if grid[nextRow][nextCol] == obstacle:
        d = (nesw.index(dir) + 1) % 4
        dir = nesw[d]
        continue
    if grid[nextRow][nextCol] != obstacle:
        if grid[nextRow][nextCol] != 0:
            possibleRowCol.append([nextRow, nextCol])
        grid[nextRow][nextCol] = 0
        row = nextRow
        col = nextCol
print("length: ", len(possibleRowCol))
print("start: ", possibleRowCol[0], "end: ", possibleRowCol[-1])
for coord in possibleRowCol:
    matrix = copy.deepcopy(grid)
    dir = startDir
    col = startCol
    row = startRow
    matrix[coord[0]][coord[1]] = '#'

    isOut = False
    isLoop = False
    i = 0
    while not (isOut or isLoop or i > 100000):
        # print(row, col, dir)
        nextRow = row
        nextCol = col
        if dir == S:
            nextRow = row + 1
        if dir == N:
            nextRow = row - 1
        if dir == E:
            nextCol = col + 1
        if dir == W:
            nextCol = col - 1

        if height - 1 < nextRow or nextRow < 0 or width - 1 < nextCol or nextCol < 0:
            isOut = True
            break
        if matrix[nextRow][nextCol] == obstacle:
            d = (nesw.index(dir) + 1) % 4
            dir = nesw[d]
            continue
        if matrix[nextRow][nextCol] != obstacle:
            isLoop = hasPassed(matrix[nextRow][nextCol], dir)
            if isLoop:
                result += 1
                break
            matrix[nextRow][nextCol] = setPassed(matrix[nextRow][nextCol], dir)
            row = nextRow
            col = nextCol
        i += 1
    if i > 100000:
        print(i)

    # print(isLoop, isOut, i)
print(result)
