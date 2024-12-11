def check(matrix, i,  j):
    # column
    if j-1 < 0:
        return 0
    if j+1 > len(matrix[i])-1:
        return 0
    # row
    if i-1 < 0:
        return 0
    if i+1 > len(matrix)-1:
        return 0
    if ((matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S') or (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M')) and ((matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S') or (matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M')):
        return 1
    return 0


file = open('input.txt')
matrix = []
result = 0
for line in file:
    matrix.extend(line)
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == 'A':
            result += check(matrix, i,  j)
print(result)
