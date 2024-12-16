file = open('input.txt')
result = 0
grid = []
orders = ''
isGrid = True
for line in file:
    if len(line) < 2:
        isGrid = False
        continue

    if isGrid:
        grid.append([a for a in line.strip()])
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
    mov = direction_map[o]
    nextPos = (robot[0]+mov[0], robot[1]+mov[1])

    while grid[nextPos[0]][nextPos[1]] == 'O':
        nextPos = (nextPos[0]+mov[0], nextPos[1]+mov[1])

    if grid[nextPos[0]][nextPos[1]] == '#':
        continue

    if grid[nextPos[0]][nextPos[1]] == '.':
        grid[robot[0]][robot[1]] = '.'
        robot = (robot[0]+mov[0], robot[1]+mov[1])
        if grid[robot[0]][robot[1]] == 'O':
            grid[nextPos[0]][nextPos[1]] = 'O'
        grid[robot[0]][robot[1]] = '@'

for i, row in enumerate(grid):
    a = ''
    for j, char in enumerate(row):
        a += char
        if char == 'O':
            result += i*100 + j
    print(a)

print(result)
