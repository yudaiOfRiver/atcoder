import io
import sys
_INPUT = """\
6 6
3
2 3 6
3
2 4 6
2
3 6
3
1 5 6
3
1 3 6
2
1 4

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N, M = map(int, input().split())
a = []
for _ in range(M):
    Ci = int(input())
    ai = list(map(int, input().split()))
    a.append(ai)

from itertools import chain,combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

x = {i for i in range(1, N+1)}
res = 0
for powerset in list(powerset(range(M))):
    xs = set()
    for p in powerset:
        xs = xs | set(a[p])

    if xs == x:
        res += 1

print(res)


