file = open('example.txt')
result = 0
keypad = [['7', '8', '9'],
          ['4', '5', '6'],
          ['1', '2', '3'],
          ['#', '0', 'A']]

arrowPad = [['#', '^', 'A'],
            ['<', 'v', '>']]


def find2d(item, matrix):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == item:
                return (i, j)
    return (-1, -1)


def findmvt(startPos, endPos):
    mvmt = ''
    di = endPos[0] - startPos[0]
    dj = endPos[1] - startPos[1]
    if di > 0:
        mvmt += 'v' * di
    elif di < 0:
        mvmt += '^' * (-di)
    if dj > 0:
        mvmt += '>' * dj
    elif dj < 0:
        mvmt += '<' * (-dj)
    return mvmt


def createSeq(seq, startPos, grid):
    start = startPos
    end = (0, 0)
    r = ''
    for char in seq:
        end = find2d(char, grid)
        r += findmvt(start, end)
        r += 'A'
        start = end
    return r


for line in file:
    print(line.strip())
    startPosKeypad = (3, 2)
    startPosArrow = (0, 2)
    endPos = (0, 0)
    seq = createSeq(line.strip(), startPosKeypad, keypad)
    print(seq)
    seq = createSeq(seq, startPosArrow, arrowPad)
    print(seq)
    seq = createSeq(seq, startPosArrow, arrowPad)
    print(seq)
    print(len(seq))

    result += len(seq)*int(line[0:3])
print(result)
