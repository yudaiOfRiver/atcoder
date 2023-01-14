import io
import sys
_INPUT = """\
4
2023
Year
New
Happy

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

N = int(input())
s = []
for i in range(N):
    si = input()
    s.append(si)

for i in range(N-1, -1, -1):
    print(s[i])

