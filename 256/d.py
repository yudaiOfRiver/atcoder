from collections import defaultdict

N = int(input())

dict = defaultdict(list)       # {number: L or R }
for _ in range(N):
    l, r = map(int, input().split())
    dict[l].append("l")
    dict[r].append("r")

numbers = list(dict.keys())
numbers.sort()
#print(dict)
#print(numbers)

count = 0
set = []

for n in numbers:
    #print(n, count)

    if dict[n] == ['r', 'l'] or dict[n] == ['l', 'r']:
        continue

    if dict[n] == ['l']:
        if count == 0:
            L = n
        count += 1

    if dict[n] == ['r']:
        count -= 1
        if count == 0:
            R = n
            print(L, R)








