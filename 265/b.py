import sys

N, M, T = map(int, input().split())
A = [-1] + list(map(int, input().split()))
XY = {}
for _ in range(M):
    XYi = list(map(int, input().split()))
    XY[XYi[0]] = XYi[1]

for i in range(1, N):
    # print("i", i)
    # print("T", T)
    T -= A[i]
    T += XY.get(i, 0)
    if T <= 0:
        print("No")
        sys.exit()

print("Yes")
