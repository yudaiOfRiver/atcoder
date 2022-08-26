X, Y, N = map(int, input().split())


res = 0
if 3 * X < Y:
    res += X * N
else:
    res += (N // 3) * Y
    res += (N % 3) * X
print(res)

