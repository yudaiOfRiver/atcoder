import io
import sys
_INPUT = """\
6
1 5 7 10 15 19
6
0
2
6
12
18
25
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

N = int(input())
A = list(map(int, input().split())) + [-10**18] + [10**18]
A.sort()
Q = int(input())

def bisearch(rate):
    l, r = 0, N+1
    while l+1 < r:
        mid = (l + r) // 2
        if rate == A[mid]:
            return mid
        elif rate < A[mid]:
            r = mid
        else:
            l = mid
    return l

for _ in range(Q):
    Bi = int(input())
    class_left = bisearch(Bi)
    print(min(Bi - A[class_left], A[class_left+1] - Bi))


