import io
import sys
_INPUT = """\
10 6
1 2 3 7 8 9
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N, M = map(int, input().split())
if M != 0:
    a = list(map(int, input().split()))
else:
    a = []

stack = []
for i in range(1, N+1):
    if i in a:
        stack.append(i)
        continue
    print(i)
    while stack:
        print(stack.pop())
