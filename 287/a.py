import io
import sys
_INPUT = """\
5
Against
Against
For
Against
For

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N = int(input())
for_ = 0
for _ in range(N):
    Si = input()
    if Si == "For":
        for_ += 1

if for_ >= (N+1)//2:
    print("Yes")
else:
    print("No")

