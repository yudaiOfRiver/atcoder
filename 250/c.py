N, Q = map(int, input().split())
x = []
for _ in range(Q):
    x.append(int(input()))

n = {}  # { index, number }
for i in range(n):
    n[i] = i

for xi in x:
    if n[xi] == N-1:
        n[N-2], n[N-1] = n[N-1], n[N-2]
    else:
        n[N], n[ind+1] = n[ind+1], n[ind]

print()



