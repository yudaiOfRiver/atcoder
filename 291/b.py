import io
import sys
_INPUT = """\
1
10 100 20 50 30
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

N = int(input())
points = [-1] + list(map(int, input().split()))
points.sort()

print(sum(points[N+1:4*N+1]) / (3*N))

