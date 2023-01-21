import io
import sys
_INPUT = """\
10 2 4 7 9
22 75 26 45 72 81 47 29 97 2

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

N, P, Q, R, S = map(int, input().split())
P -= 1
Q -= 1
R -= 1
S -= 1

A = list(map(int, input().split()))

B = A[:P] + A[R:S+1] + A[Q+1:R] + A[P:Q+1] + A[S+1:]
print(*B)
