import io
import sys
_INPUT = """\
8
national

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N = int(input())
S = input()

res = ""
i = 0
while i < N:
    if S[i:i+2] == 'na':
            res += "nya"
            i += 2
            continue
    res += S[i]
    i += 1

print(res)
