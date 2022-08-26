N, M = map(int, input().split())
X = list(map(int, input().split()))

Y = [0] * (N+1)
for _ in range(M):
    c, y = map(int, input().split())
    Y[c] = y

INF = float('inf')
DP = [[-INF] * (N+1) for _ in range(N+1)]
DP[0][0] = 0

for i in range(N):
    for j in range(N):
        DP[i+1][j+1] = DP[i][j] + X[i] + Y[j+1]
        DP[i+1][0] = max(DP[i][j], DP[i+1][0])
        #print(i, j)
        #print(DP)
        #print("--------")
    #print("============")

#print(DP)

res = max(DP[-1])
print(res)
