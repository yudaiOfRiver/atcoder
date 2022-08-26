n, X = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    if X & (1<<i):
        res += a[i]

print(res)
