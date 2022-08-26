N, M = map(int, input().split())
#N = 2
#M = 3

res = []

def dfs(line):
    if len(line) == N:
        res.append(line[:])
        return

    tail = line[-1]
    for j in range(tail+1, M+1):
        line.append(j)
        dfs(line)
        line.pop(-1)
        #print(res)

for i in range(1, M+1):
    dfs([i])

for r in res:
    print(*r)
