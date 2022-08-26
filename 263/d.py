N, L, R = map(int, input().split())
A = [0] + list(map(int, input().split()))

#N, L, R = 10, -5, -3
#A = [0, 9, -6, 10, -1, 2, 10, -1, 7, -15, 5]
#N, L, R = 4, 10, 10
#A = [0, 1, 2, 3, 4]

INF = float('inf')
DP = [[INF] * (N+1) for _ in range(N+1)]
DP[0][0] = sum(A)
for i in range(1, N+1):
    DP[i][0] = DP[i-1][0] - A[i] + R

for i in range(1, N+1):
    DP[0][i] = DP[0][i-1] - A[N-i+1] + L


for y in range(1, N+1):
    for x in range(1, N+1-y):
        DP[x][y] = min(DP[x-1][y]-A[x]+R, DP[x][y-1]-A[N-y+1]+L)

curMin = float('inf')
for i in range(N+1):
    curMin = min(curMin, min(DP[i]))

print(curMin)

