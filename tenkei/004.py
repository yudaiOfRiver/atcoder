import io
import sys
_INPUT = """\
10 10
83 86 77 65 93 85 86 92 99 71
62 77 90 59 63 76 90 76 72 86
61 68 67 79 82 80 62 73 67 85
79 52 72 58 69 67 93 56 61 92
79 73 71 69 84 87 98 74 65 70
63 76 91 80 56 73 62 70 96 81
55 75 84 77 86 55 96 79 63 57
74 95 82 95 64 67 84 64 93 50
87 58 76 78 88 84 53 51 54 99
82 60 76 68 89 62 76 86 94 89
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

H, W = map(int, input().split())
A = []
for _ in range(H):
    Ai = list(map(int, input().split()))
    A.append(Ai)


row_sum = [0] * W
col_sum = [0] * H
for i in range(H):
    for j in range(W):
        col_sum[i] += A[i][j]
        row_sum[j] += A[i][j]

ans = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = row_sum[j] + col_sum[i] - A[i][j]

for a in ans:
    print(*a)



