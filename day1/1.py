file = open('input.txt')
left_list = []
right_list = []
for line in file:
    a = line.split()
    left_list.extend(int(a[0]))
    right_list.extend(int(a[1]))
left_list.sort()
right_list.sort()

diff = sum(abs(a-b) for a, b in zip(right_list, left_list))
print(diff)
