H, W = map(int, input().split())

G = []
for _ in range(H):
    Gi = list(input())
    G.append(Gi)
#print(G)

# H, W = 2, 3
# G = [['R', 'R', 'D'], ['U', 'L', 'L']]
directions = {'U': [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}

seen = set()
def dfs(i, j):
    if (i, j) in seen:
        return -1

    seen.add((i, j))
    action = G[i][j]
    i_next = i + directions[action][0]
    j_next = j + directions[action][1]

    if i_next in range(H) and j_next in range(W):
        return dfs(i_next, j_next)
    else:
        return i, j

res = dfs(0, 0)
#print(res)
if res == -1:
    print(-1)
else:
    print(res[0]+1, res[1]+1)



