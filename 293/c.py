import io
import sys
_INPUT = """\
2 3
4 2 2
2 1 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
from itertools import combinations

H, W = map(int, input().split())
A = [[-1]*W]
for _ in range(H):
    A_i = [-1] + list(map(int, input().split()))
    A.append(A_i)

cnt = 0
for right in list(combinations(range(1, H+W-1), H-1)):
    i, j = 1, 1
    visited = set()
    visited.add(A[i][j])

    ok = True
    for k in range(1, H+W-1):
        if k in right:
            i += 1
        else:
            j += 1
        if A[i][j] in visited:
            ok = False
            break
        visited.add(A[i][j])

    if ok:
        cnt += 1

print(cnt)


