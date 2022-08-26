N = int(input())
A = list(map(int, input().split()))

set = []

for ai in A:
    set.append(0)
    for i in range(len(set)):
        set[i] += ai


P = 0
for s in set:
    if s >= 4:
        P += 1

print(P)


