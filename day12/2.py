def spread(grid, i, j, char):
    arr = set()
    if grid[i][j] == char.lower():
        return arr
    if grid[i][j] != char:
        return arr
    grid[i][j] = char.lower()
    arr.update({(i, j)})
    arr.update(spread(grid, i+1, j, char))
    arr.update(spread(grid, i-1, j, char))
    arr.update(spread(grid, i, j+1, char))
    arr.update(spread(grid, i, j-1, char))
    return arr


def minMax(arr):
    min_x = min(coord[0] for coord in arr)
    max_x = max(coord[0] for coord in arr)

    # Find min and max for y-coordinates
    min_y = min(coord[1] for coord in arr)
    max_y = max(coord[1] for coord in arr)
    return min_x, max_x, min_y, max_y


file = open('input.txt')
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
        arr = spread(grid, i, j, grid[i][j])
        area = len(arr)
        px, gx, py, gy = minMax(arr)
        char = grid[i][j].lower()
        # find the number of border :
        border = 0
        for y in range(py-1, gy + 1):
            leftC = False
            rightC = False

            for x in range(px, gx+1):
                left = grid[x][y]
                right = grid[x][y+1]
                if left != char and right != char:
                    leftC = False
                    rightC = False
                    continue
                if left == char and right == char:
                    leftC = False
                    rightC = False
                    continue
                if left == char:
                    if not leftC:
                        border += 1
                    leftC = True
                    rightC = False
                    continue
                if right == char:
                    if not rightC:
                        border += 1
                    rightC = True
                    leftC = False
                    continue

        for x in range(px-1, gx + 1):
            upC = False
            downC = False

            for y in range(py, gy+1):
                up = grid[x][y]
                down = grid[x+1][y]
                if up != char and down != char:
                    upC = False
                    downC = False
                    continue
                if up == char and down == char:
                    upC = False
                    downC = False
                    continue
                if up == char:
                    if not upC:
                        border += 1
                    upC = True
                    downC = False
                    continue
                if down == char:
                    if not downC:
                        border += 1
                    downC = True
                    upC = False
                    continue

        # print(area, border, char)
        result += area*border
        for coord in arr:
            grid[coord[0]][coord[1]] = '.'


# for gr in grid:
#     print(''.join(gr))
print(result)
