N, W = map(int, input().split())
A = list(map(int, input().split()))

res = set()
# 1個
for i in range(N):
    if A[i] <= W:
        res.add(A[i])

# 2個
for i in range(N):
    for j in range(i+1, N):
        if A[i] + A[j] <= W:
            res.add(A[i] + A[j])

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if A[i] + A[j] + A[k] <= W:
                res.add(A[i] + A[j] + A[k])

print(len(res))




