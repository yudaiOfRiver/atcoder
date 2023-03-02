import io
import sys
_INPUT = """\
4 6
1 2
1 2
2 3
2 3
3 4
3 4

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
from collections import defaultdict
import sys

from collections import deque, defaultdict

def topological_sort(next, in_deg, N):
    # next[i] : 頂点i からの到達可能集合
    # in_deg[i] : 頂点i の入次数
    # N : 頂点数
    res = [0] * N

    topo_sort = [v for v in range(N) if in_deg[v] == 0]
    if len(topo_sort) != 1:
        return False

    res[topo_sort[0]] = 1
    val = 2
    q = deque(topo_sort)

    while q:
        if len(q) != 1:
            return False
        v = q.popleft()
        for n in next[v]:
            in_deg[n] -= 1
            if in_deg[n] == 0:
                q.append(n)
                topo_sort.append(n)

                res[n] = val
        val += 1
    return res



N, M = map(int, input().split())
in_deg = defaultdict(lambda : 0)
next = defaultdict(list)

for _ in range(M):
    Xi, Yi = map(int, input().split())
    Xi -= 1
    Yi -= 1
    next[Xi].append(Yi)
    in_deg[Yi] += 1

res = topological_sort(next, in_deg, N)
if res:
    print("Yes")
    print(*res)
else:
    print("No")
