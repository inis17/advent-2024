def spread(grid, i, j, char):
    area = 0
    perimeter = 0
    if grid[i][j] == char.lower():
        return 0, 0
    if grid[i][j] != char:
        return 0, 1
    grid[i][j] = char.lower()
    area += 1
    a, b = spread(grid, i+1, j, char)
    area += a
    perimeter += b
    a, b = spread(grid, i-1, j, char)
    area += a
    perimeter += b
    a, b = spread(grid, i, j+1, char)
    area += a
    perimeter += b
    a, b = spread(grid, i, j-1, char)
    area += a
    perimeter += b
    return area, perimeter


file = open('input.txt')
area, perimeter = 0, 0
grid = []
result = 0
for line in file:
    grid.append(list(f".{line.strip()}."))

grid.insert(0, ['.'] * len(grid[0]))
grid.append(['.'] * len(grid[0]))


width = len(grid[0])
height = len(grid)

for i in range(1, height-1):
    for j in range(1, width-1):
        if grid[i][j] == '.' or grid[i][j].islower():
            continue
        area, perimeter = spread(grid, i, j, grid[i][j])
        result += area*perimeter


# for gr in grid:
#     print(''.join(gr))
print(result)
