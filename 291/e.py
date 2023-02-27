import io
import sys
_INPUT = """\
3 2
3 1
2 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
from collections import defaultdict
import sys

N, M = map(int, input().split())
in_deg = defaultdict(lambda : 0)
next = defaultdict(list)


for _ in range(M):
    Xi, Yi = map(int, input().split())
    Xi -= 1
    Yi -= 1
    next[Xi].append(Yi)
    in_deg[Yi] += 1

path = []
def dfs(now):
    count = 0
    for next in next[now]:
        in_deg[next] -= 1
        if in_deg[next] == 0:
            count += 1
            if count == 2:
                print("No")
                sys.exit()
                

dfs()
print("Yes")
print(*path)
