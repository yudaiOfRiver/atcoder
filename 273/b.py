import sys

X, K = input().split()
K = int(K)

if K > len(X):
    print(0)
    sys.exit()

X = int(X)

def func(n):
    n = int(n)
    if n >= 5:
        return 10-n
    else:
        return -n


for i in range(1, K+1):
    Xi = X % (10**i)
#    print("Xi", Xi)
    Xi = str(Xi)[0]
#    print("XI", Xi)
    added = func(Xi)
#    print("added", added)
    X += added * (10**(i-1))
print(X)




