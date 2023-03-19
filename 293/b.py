import io
import sys
_INPUT = """\
5
3 1 4 5 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N = int(input())
A = [-1] + list(map(int, input().split()))

for i in range(1, N+1):
    Ai = A[i]
    if Ai == 0:
        continue

    A[Ai] = 0

K = 0
X = []
for i in range(1, N+1):
    if A[i] > 0:
        K += 1
        X.append(i)

print(K)
print(*X)




