import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
X = []
for _ in range(N):
    X.append(list(map(int, input().split())))

res2 = 0
for i in range(N):
    if i+1 in A:
        continue
    mini = float('inf')
    for j in A:
        l = (X[i][0]-X[j-1][0])**2 + (X[i][1]-X[j-1][1])**2
        mini = min(mini, l)
    res2 = max(res2, mini)
    
print(math.sqrt(res2))


