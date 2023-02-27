import io
import sys
_INPUT = """\
Zz
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
import sys

S = input()

for i in range(len(S)):
    if S[i].isupper():
        print(i+1)
        sys.exit()



