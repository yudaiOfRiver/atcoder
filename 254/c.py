import sys

N, K = map(int, input().split())
q, r = N // K, N % K

a = list(map(int, input().split()))

group = [[] for _ in range(K)]

i = 0
while i < len(a):
    group[i % K].append(a[i])
    i += 1

for i in range(K):
    group[i].sort()

j = 0
while j < N-1:
    gid = j % K
    ind = j // K
    if gid == K-1:
        if group[gid][ind] > group[0][ind+1]:
            print("No")
            sys.exit()
    elif group[gid][ind] > group[gid+1][ind]:
        print("No")
        sys.exit()
    j += 1

print("Yes")








