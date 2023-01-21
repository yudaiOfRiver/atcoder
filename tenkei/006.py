import io
import sys
_INPUT = """\
14 5
kittyonyourlap

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#


N, K = map(int, input().split())
S = input()

nxt = [[N] * 26 for _ in range(N+1)]
# nxt[i][c] : i文字目以降で、文字c が最初に現れる添字

for i in range(N-1, -1, -1):
    for j in range(26):
        nxt[i][j] = nxt[i+1][j]
    nxt[i][ord(S[i]) - ord('a')] = i

res = ""
now = 0
for l in range(K):
    for c in range(26):
        if nxt[now][c] <= N - (K - l):
            res += chr(ord('a') + c)
            now = nxt[now][c] + 1
            break
print(res)



