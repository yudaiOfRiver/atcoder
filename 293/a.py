import io
import sys
_INPUT = """\
atcoderbeginnercontest
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

S = input()

for i in range(0, len(S), 2):
    S = S[:i] + S[i+1] + S[i] + S[i+2:]
print(S)


