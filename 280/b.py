N = int(input())
S = [0] + list(map(int, input().split()))

res = [0] * N
for i in range(N):
    res[i] = S[i+1] - S[i]
print(*res)
