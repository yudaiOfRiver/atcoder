N, M = map(int, input().split())

u_v = []
for _ in range(M):
    u, v = map(int, input().split())
    u_v.append((u, v))

res = 0
for i in range(N+1):
    for j in range(i+1, N+1):
        for k in range(j+1, N+1):
            #print(i, j, k)
            if ((i, j) in u_v or (j, i) in u_v) and ((j, k) in u_v or (k, j) in u_v) and ((k, i) in u_v or (i, k) in u_v):
                res += 1
print(res)
