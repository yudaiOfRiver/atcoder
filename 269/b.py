from collections import Counter

S = []
A = 0
base_line = '..........'
line = 'aaaa'
count = 0
for i in range(10):
    Si = input()
    if Si == base_line:
        continue
    elif Si == line:
        count += 1
        continue
    else:
        line = Si
        A = i
        count += 1

A += 1
B = A + count -1

cur = 0
tmp = 'a'
for i in range(10):
    if tmp != '#' and line[i] == '#':
        C = i+1
        cur += 1
        tmp = line[i]
    elif tmp == '#' and line[i] == '#':
        cur += 1
D = C + cur-1

print(A, B)
print(C, D)






