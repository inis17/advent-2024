def isSafe(numList):
    isSafe = True
    isIncreasing = numList[0] < numList[1]
    for i in range(1, len(numList)):
        diff = abs(numList[i-1] - numList[i])
        if diff == 0 or diff > 3:
            isSafe = False
            break
        if isIncreasing != (numList[i-1] < numList[i]):
            isSafe = False
            break
    return isSafe


file = open('input.txt')
left_list = []
right_list = []
result = 0
for line in file:
    numList = [int(num) for num in line.split()]
    safe = isSafe(numList)
    if safe:
        result = result + 1
        continue
    for i, num in enumerate(numList):
        copyList = numList.copy()
        del copyList[i]
        if isSafe(copyList):
            # print(copyList, numList, i)
            result = result + 1
            break

print(result)
