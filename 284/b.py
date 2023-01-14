import io
import sys
_INPUT = """\
4
3
1 2 3
2
20 23
10
6 10 4 1 5 9 8 6 5 1
1
1000000000
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
T = int(input())
for i in range(T):
    N = int(input())
    out = 0
    A = list(map(int, input().split()))
    for j in range(N):
        if A[j] % 2 == 1:
            out += 1
    print(out)


