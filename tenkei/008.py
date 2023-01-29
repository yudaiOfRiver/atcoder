import io
import sys
_INPUT = """\
10
attcordeer
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
from collections import defaultdict
from pprint import pprint

N = int(input())
S = input()

target = "atcoder"
DP = [[False] * (N+1) for _ in range(len(target))]
DP[0][0] = True

for i in range(1, N+1):
    for j in range(len(target)):
        DP[i+1][j] = (DP[i][j] and S[i]==target[j]) or DP[i][j]
    pprint(DP)




