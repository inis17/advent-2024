from collections import defaultdict
from math import gcd
file = open('input.txt')
result = 0
grid = []
antennas = defaultdict(list)
for i, line in enumerate(file):
    grid.append(list(line.strip()))
    for j, char in enumerate(line.strip()):
        if char == '.':
            continue
        antennas[char].append([i, j])

for antenna in antennas:
    print(antenna)
    for i, coor1 in enumerate(antennas[antenna]):
        for idx, coor2 in enumerate(antennas[antenna]):
            if idx == i:
                continue
            # create the '#' point
            vx = coor1[0] - coor2[0]
            vy = coor1[1] - coor2[1]
            if vx == 0 and vy != 0:
                vy = 1
            if vy == 0 and vx != 0:
                vx = 1
            if vx != 0 and vy != 0:
                a = gcd(vx, vy)
                vx = vx/a
                vy = vy/a
            inbound = True
            n = 0
            while inbound:
                x = int(coor1[0]+vx*n)
                y = int(coor1[1]+vy*n)
                if x > len(grid) - 1 or x < 0:
                    inbound = False
                    break
                if y > len(grid[x]) - 1 or y < 0:
                    inbound = False
                    break
                if grid[x][y] != '#':
                    result += 1
                    grid[x][y] = '#'
                n += 1
            inbound = True
            n = 1
            while inbound:
                x = int(coor1[0]-vx*n)
                y = int(coor1[1]-vy*n)
                if x > len(grid) - 1 or x < 0:
                    inbound = False
                    break
                if y > len(grid[x]) - 1 or y < 0:
                    inbound = False
                    break
                if grid[x][y] != '#':
                    result += 1
                    grid[x][y] = '#'
                n += 1

for line in grid:
    print(line)

print(result)
