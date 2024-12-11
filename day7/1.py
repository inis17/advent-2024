import re


def calc(first, others, ops, target):
    for o in ops:
        res = first
        if o == '+':
            res += others[0]
        if o == '*':
            res *= others[0]
        if o == '|':
            res = int(str(res) + str(others[0]))

        if len(others) == 1:
            if res == target:
                return True
            continue
        if res > target:
            continue
        subset = slice(1, len(others))
        isTrue = calc(res, others[subset], ops, target)
        if isTrue:
            return True


# from itertools import product
tot = []
file = open('input.txt')
for line in file:
    result, *num = map(int, re.findall('\d+', line))
    operation = ['+', '*', '|']
    if calc(num[0], num[slice(1, len(num))], operation, result):
        tot.extend(result)


print(sum(tot))
