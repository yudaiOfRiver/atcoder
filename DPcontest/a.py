import io
import sys
_INPUT = """\
4
10 30 40 20
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

from numpy import abs

def cost(i, j):
    return abs(h[i] - h[j])

N = int(input())
h = [-1] + list(map(int, input().split()))

INF = 10**10
DP = [-1] + [INF] * N
DP[N] = 0
DP[N-1] = abs(h[N-1] - h[N])

for i in range(N-2, 0, -1):
    DP[i] = min(DP[i+1]+cost(i, i+1), DP[i+2]+cost(i, i+2))

print(DP[1])
