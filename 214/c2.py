# 累積和的に考える

#N = int(input())
#S = [-1] + list(map(int, input().split()))
#T = [-1] + list(map(int, input().split()))

N = 3
S = [4, 1, 5]
T = [3, 10, 100]

S = S + [0]
for i in range(1, N+1):
    S[i] += S[i-1]
print(S)


#res = T
#for i in range(N):
#    for j in range(N):
#        if i > j:
#            from_j = T[j] + (i-j)*S([i]-S[j])
#            res[i] = min(res[i], from_j)
#        elif i < j:
#            from_j = T[j] + (N-(j-i))*((S[N]-S[j]) + (S[i]-S[N]))
