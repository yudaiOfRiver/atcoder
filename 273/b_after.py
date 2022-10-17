X, K = map(int, input().split())

for i in range(1, K+1):
    X = X + (5 * 10**(i-1))
#    print(X)
    X = X // 10**i
#    print(X)
    X = X * 10**i
#    print(X)
#    print("======")

print(X)
