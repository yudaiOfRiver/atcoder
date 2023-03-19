import io
import sys
_INPUT = """\
10 4
2 7 1 8 2 8 1 8 2 8
1 10
1 9
2 10
5 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
ele = list()
cnt = defaultdict(lambda : 0)

for i in range(N):
    cnt[A[i]] += 1


for k,v in cnt.items():
    if v >= 3:
        ele.append(v)

for i in range(Q):
    li, ri = map(int, input().split())



