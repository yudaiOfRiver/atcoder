N = int(input())
H = list(map(int, input().split()))

res = 0
cur = 0
tmp = H[0]
for i in range(1, N):
    if tmp >= H[i]:
        cur += 1
    else:
        cur = 0
    tmp = H[i]

    res = max(res, cur)
print(res)




