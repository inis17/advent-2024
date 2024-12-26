import re
f = open('2').read().strip().split('\n')
for line in f:
    a, o, b, c = re.findall('\w+')
    number = re.findall('\d+')[0]
    temp = [a, b]
    temp.sort()
