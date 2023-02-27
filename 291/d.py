import io
import sys
_INPUT = """\
3
1 2
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N = int(input())
head, tail = map(int, input().split())
h_cnt, t_cnt = 1, 1
for i in range(1, N):
    pre_head, pre_tail = head, tail
    pre_h_cnt, pre_t_cnt = h_cnt, t_cnt
    h_cnt, t_cnt = 0, 0
    head, tail = map(int, input().split())

    if head != pre_head:
        h_cnt += pre_h_cnt
    if head != pre_tail:
        h_cnt += pre_t_cnt
    if tail != pre_head:
        t_cnt += pre_h_cnt
    if tail != pre_tail:
        t_cnt += pre_t_cnt
    # print(h_cnt, t_cnt)

print((h_cnt+t_cnt) % 998244353 )













