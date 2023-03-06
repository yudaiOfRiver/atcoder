import io
import sys
_INPUT = """\
13 16
7 9
7 11
3 8
1 13
11 11
6 11
8 13
2 11
3 3
8 12
9 11
1 11
5 13
3 12
6 9
1 10
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

from collections import defaultdict
import sys

class UnionFind():
    def __init__(self, n) -> None:
        self.roots = [-1] * n
        self.edges = [0] * n # 辺の数を表す。根のインデックスのみ有効。

    def find(self, x):
        if self.roots[x] < 0:
            return x
        else:
            self.roots[x] = self.find(self.roots[x])
            return self.roots[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            self.edges[x] += 1
            return

        if self.roots[x] > self.roots[y]:
            x, y = y, x

        self.roots[x] += self.roots[y]
        self.roots[y] = x
        self.edges[x] += self.edges[y]
        self.edges[x] += 1


N, M = map(int, input().split())
uf = UnionFind(N)

for i in range(M):
    ui, vi = map(int, input().split())
    ui -= 1
    vi -= 1
    uf.union(ui, vi)


#print(uf.roots)
#print(uf.edges)
for i in range(N):
    if uf.roots[i] > 0:
        continue

    if uf.roots[i] != - uf.edges[i]:
        print("No")
        sys.exit()

print("Yes")


