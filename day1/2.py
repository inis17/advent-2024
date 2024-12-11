from collections import Counter

file = open('input.txt')
left_list = []
right_list = []
for line in file:
    a = line.split()
    left_list.extend(int(a[0]))
    right_list.extend(int(a[1]))
counter = Counter(right_list)
print(counter)
sum = 0
for element in left_list:
    sum += element * counter.get(element, 0)
print(sum)
