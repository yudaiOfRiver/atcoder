import io
import sys
_INPUT = """\
10 4
40 10 20 70 80 10 20 70 80 60
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

def cost(i, j):
    return h[i] - h[j] if h[i] > h[j] else h[j] - h[i]

N, K = map(int, input().split())
h = [-1] + list(map(int, input().split()))

INF = 10**10
DP = [-1] + [INF] * (N)
DP[N] = 0

for i in range(N-1, 0, -1):
    for j in range(1, K+1):
        if i+j > N:
            continue
        DP[i] = min(DP[i], DP[i+j]+cost(i, i+j))

print(DP[1])


