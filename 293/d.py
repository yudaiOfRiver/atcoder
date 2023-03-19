import io
import sys
_INPUT = """\
7 0
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
from collections import defaultdict

class UnionFind():

    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())

    def group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n+1):
            group_members[self.find(member)].append(member)
        return group_members



N, M = map(int, input().split())

degree = defaultdict(lambda: 0)
uf = UnionFind(N)
for _ in range(M):
    Ai, Bi, Ci, Di = input().split()
    Ai = int(Ai); Ci = int(Ci)
    uf.unite(Ai, Ci)
    degree[Ai] += 1
    degree[Ci] += 1


noncycle = 0
for root, members in uf.group_members().items():
    if root == 0:
        continue

    for mem in members:
        if degree[mem] != 2:
            noncycle += 1
            break

groups = uf.group_size()
print(groups-noncycle-1, noncycle)




