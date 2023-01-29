import io
import sys
_INPUT = """\
a?b?c?def
ab?
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
S = input()
T = input()
len_T = len(T)

S = "?" + S + "?"
T = "?" + T + "?"

pre = [True] + [False]*len_T
suf = [False]*len_T + [True]
for i in range(1, len_T+1):
    if S[i] == T[i] or S[i] == "?" or T[i] == "?":
        pre[i] = (True and pre[i-1])
    if S[-1-i] == T[-1-i] or S[-1-i] == "?" or T[-1-i] == "?":
        suf[-1-i] = (True and suf[-i])

for x in range(len_T+1):
    if pre[x] and suf[x]:
        print("Yes")
    else:
        print("No")


