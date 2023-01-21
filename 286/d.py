import io
import sys
_INPUT = """\
2 19
2 3
5 6
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

N, X = map(int, input().split())

coins = []
for _ in range(N):
    Ai, Bi = map(int, input().split())
    for __ in range(Bi):
        coins.append(Ai)

ok = [False] * (X+1)
ok[0] = True
print(coins)
for c in coins:
    for j in range(X, c-1, -1):
        ok[j] |= ok[j-c]

if ok[X]:
    print("Yes")
else:
    print("No")




