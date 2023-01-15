import io
import sys
_INPUT = """\
20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

N, L = map(int, input().split())
K = int(input())

A = [0] + list(map(int, input().split())) + [L]

def ok(l):
    cur_len = 0
    cnt = 0
    for i in range(N+1):
        cur_len += A[i+1] - A[i]
        if cur_len >= l:
            cur_len = 0
            cnt += 1
        if cnt >= K+1:
            return True
    return False

bottom, top = 0, L+1
while top-bottom > 1:
    mid = (top+bottom) // 2
    if ok(mid): bottom = mid
    else: top = mid

print(bottom)

