from collections import defaultdict
import sys

H, W = map(int, input().split())

Scnt = ["" for _ in range(W)]
Tcnt = ["" for _ in range(W)]


for i in range(H):
    Si = input()
    Sj = ""
    for j in range(W):
        if Si[j] == '#': Scnt[j] += str(i)


for i in range(H):
    Ti = input()
    for j in range(W):
        if Ti[j] == '#': Tcnt[j] += str(i)

for j in range(W):
    try:
        Scnt.remove(Tcnt[j])
    except ValueError:
        print("No")
        sys.exit()

print("Yes")


