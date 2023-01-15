import io
import sys
_INPUT = """\
6
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

from itertools import combinations
N = int(input())
pare = []

for x in list(combinations(range(N), N//2)):
    p = ")" * N
    for xi in x:
        p = p[:xi] + "(" + p[xi+1:]
    cnt = 0

    ok = True
    for pi in p:
        if pi == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            ok = False
    if ok: print(p)



