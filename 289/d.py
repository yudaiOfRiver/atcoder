import io
import sys
_INPUT = """\
4
2 5 7 8
5
2 9 10 11 19
20
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

reachable = [False] * (X+1)
reachable[X] = True

mochi = [True] * (X+1) # 餅があるとこが False
for Bi in B:
    mochi[Bi] = False

for i in range(X-1, -1, -1):
    for Ai in A:
        if i+Ai <= X:
            reachable[i] = (reachable[i] or reachable[i+Ai])
    reachable[i] = reachable[i] and mochi[i]

if reachable[0]:
    print("Yes")
else:
    print("No")

