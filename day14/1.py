import numpy as np
file = open('input.txt')
result = 0
width = 101
height = 103
seconds = 00
robots = []
for line in file:
    p, v = line.strip().split(' ')
    px, py = [int(n) for n in p[2::].split(',')]
    vx, vy = [int(n) for n in v[2::].split(',')]
    robots.append([px, py, vx, vy])

    nx = 0
    ny = 0
    vx = 10000000
    vy = 100000000
for n in range(8087, 8088):

    pos = []
    for r in robots:
        fx = (r[0]+n*r[2]) % width
        fy = (r[1]+n*r[3]) % height
        pos.append([fx, fy])

    v = np.var(pos, axis=0)
    print(n, v)
    for y in range(0, height):
        line = ''
        for x in range(0, width):
            if [x, y] in pos:
                line += '@'
                continue
            line += ' '
        print(line)


print(nx, ny)
# print(pos)53
# the x poition are width periodic (means every width second the x position repeats)
# the y poition are width periodic (means every width second the y position repeats)
# calculatingthe variance over the x and y axis, we find that some specific value or reminder along x,y
# we then have the relation : x = rx+k*width and y=ry+p*height with (k,p) int
# we look for the smallest k,p so that x and y are equals (means we are at a common value)
