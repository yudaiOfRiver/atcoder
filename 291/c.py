import io
import sys
_INPUT = """\
20
URDDLLUUURRRDDDDLLLL
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N = int(input())
S = input()

visited = set()
directions = {"R": (1, 0), "D": (0, -1), "L": (-1, 0), "U": (0, 1)}

x, y = 0, 0
visited.add((x, y))
for Si in S:
    (dx, dy) = directions[Si]
    x += dx; y += dy
    visited.add((x, y))

if len(visited) == N+1:
    print("No")
else:
    print("Yes")




