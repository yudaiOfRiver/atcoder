N, X, Y = map(int, input().split())
A = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    ui, vi = map(int, input().split())
    A[ui][vi] = 1
    A[vi][ui] = 1

res = []
seen = set()
def dfs(x, y):
    if x == y:
        return res

    for i in range(1, N+1):
        if A[x][i] and i not in seen:
            seen.add(i)
            res.add(i)

            tmp = dfs(i, y)
            if res == tmp:
                return res
    res.pop(-1)
    return res

dfs(X, Y)
















