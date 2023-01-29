import io
import sys
_INPUT = """\
5 4
1 2
2 3
3 4
4 5
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
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N, M = map(int, input().split())
if N-1 != M:
    print("No")
    exit()

degree = defaultdict(lambda: 0)
uf = UnionFind(N)
for _ in range(M):
    ui, vi = map(int, input().split())
    uf.unite(ui, vi)
    degree[ui] += 1
    degree[vi] += 1

#print(uf.group_size())

if uf.group_size() != 2:
    print("No")
    exit()


deg_num = defaultdict(lambda: 0)
for deg in degree.values():
    deg_num[deg] += 1


for k, v in deg_num.items():
    if k == 1 and v == 2:
        continue
    elif k == 2 and v == (N-2):
        continue
    else:
        print("No")
        exit()
print("Yes")
