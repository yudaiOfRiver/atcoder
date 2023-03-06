import io
import sys
_INPUT = """\
3
1 1
3 1

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

from collections import defaultdict

cards = defaultdict(lambda : 0)
N, Q = map(int, input().split())

for i in range(Q):
    n, x = map(int, input().split())
    if n == 1:
        cards[x] += 1
    if n == 2:
        cards[x] += 2
    if n == 3:
        if cards[x] >= 2:
            print("Yes")
        else:
            print("No")

