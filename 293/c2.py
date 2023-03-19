import io
import sys
_INPUT = """\
3 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
H, W = map(int, input().split())
A = []
for _ in range(H):
    Ai = list(map(int, input().split()))
    A.append(Ai)

def dfs(i, j, visited):
    if (i, j) in visited: return 0

    visited.add((i, j))
    cnt = 0
    if (i, j) == (H, W):
        return 1

    if i < H:
        cnt += dfs(i+1, j, visited)
        visited.remove((i+1, j))
    if j < W:
        cnt += dfs(i, j+1, visited)
        visited.remove((i, j+1))

    return cnt

print(dfs(1, 1, set()))


