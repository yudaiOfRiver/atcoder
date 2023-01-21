import io
import sys
_INPUT = """\
8 1000000000 1000000000
bcdfcgaa
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

N, A, B = map(int, input().split())
S = input()

res = float('inf')
for r in range(N):
    cost = r * A
    for i in range(N):
        op = (N-1) - i
        if i < op and (S[i] != S[op]):
            cost += B

    S = S[1:] + S[0]
    res = min(res, cost)

print(res)

