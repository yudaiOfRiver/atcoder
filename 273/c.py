from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A.sort()
c = Counter(A)

kind = list(set(A))
kind.sort()

for i in range(len(kind)-1, -1, -1):
    ki = kind[i]
    print(c[ki])

for _ in range(N-len(kind)):
    print(0)


