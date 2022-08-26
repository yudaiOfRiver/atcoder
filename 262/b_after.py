N, M = map(int, input().split())

mat = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    mat[u][v] = 1
    mat[v][u] = 1

res = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if mat[i][j] and mat[j][k] and mat[k][i]:
                res += 1

print(res)
