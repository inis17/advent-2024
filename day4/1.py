def checkE(matrix, i, j, word):
    if len(word)+j > len(matrix[i]):
        return 0
    for n, char in enumerate(word):
        if matrix[i][j+n] != char:
            return 0
    print(i, j)
    return 1


def checkW(matrix, i, j, word):
    if j-len(word) < 0:
        return 0
    for n, char in enumerate(word):
        if matrix[i][j-n] != char:
            return 0
    print(i, j)
    return 1


def checkS(matrix, i, j, word):
    if i+len(word) > len(matrix):
        return 0
    for n, char in enumerate(word):
        if matrix[i+n][j] != char:
            return 0
    print(i, j)
    return 1


def checkN(matrix, i, j, word):
    if i-len(word) < 0:
        return 0
    for n, char in enumerate(word):
        if matrix[i-n][j] != char:
            return 0
    print(i, j)
    return 1


def check(matrix, i, di, j, dj, word):
    # column
    if j+dj*(len(word) - 1) < 0:
        return 0
    if j+dj*(len(word)) > len(matrix[i]):
        return 0
    # row
    if i+di*(len(word) - 1) < 0:
        return 0
    if i+di*(len(word)) > len(matrix):
        return 0
    for n, char in enumerate(word):
        if matrix[i+n*di][j+n*dj] != char:
            return 0
    return 1


file = open('input.txt')
matrix = []
result = 0
for line in file:
    # NOTE: The matrix is inverted (line are accessed with j instead of i)
    matrix.extend(line)
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == 'X':
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    result += check(matrix, i, di, j, dj, 'XMAS')
print(result)
