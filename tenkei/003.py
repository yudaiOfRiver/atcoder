import io
import sys
_INPUT = """\
3

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

sys.setrecursionlimit(10**6)
N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N-1):
    Ai, Bi = map(int, input().split())
    Ai -= 1
    Bi -= 1
    edges[Ai].append(Bi)
    edges[Bi].append(Ai)

dist = [0] * N
def dfs(x, last=-1):
    global dist
    for next in edges[x]:
        if next == last:
            continue
        dist[next] = dist[x] + 1
        dfs(next, x)

dfs(0)
max_dist = max(dist)
idx = dist.index(max_dist)
dist[idx] = 0
dfs(idx)
print(max(dist)+1)


