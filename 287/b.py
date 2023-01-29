import io
import sys
_INPUT = """\
4 4
000000
123456
987111
000000
000
111
999
111
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#`
N, M = map(int, input().split())
S = []
for _ in range(N):
    Si = int(input()[3:])
    S.append(Si)

T = set()
for _ in range(M):
    Ti = int(input())
    T.add(Ti)


res = 0
for Si in S:
    if Si in T:
        res += 1
print(res)



