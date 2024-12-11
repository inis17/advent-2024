def numPath(grid, x, y, value):
    if value == 9:
        return 1
    result = 0
    if x - 1 >= 0:
        if grid[x-1][y] == value + 1:
            result += (numPath(grid, x-1, y, value + 1))
    if x + 1 < len(grid):
        if grid[x+1][y] == value + 1:
            result += (numPath(grid, x+1, y, value + 1))
    if y - 1 >= 0:
        if grid[x][y-1] == value + 1:
            result += (numPath(grid, x, y-1, value + 1))
    if y + 1 < len(grid[x]):
        if grid[x][y+1] == value + 1:
            result += (numPath(grid, x, y+1, value + 1))
    return result


file = open('input.txt')
result = 0
grid = []
for line in file:
    grid.append([int(x) for x in line.strip()])

for x, row in enumerate(grid):
    for y, col in enumerate(row):
        if col == 0:
            result += (numPath(grid, x, y, 0))

print(result)
