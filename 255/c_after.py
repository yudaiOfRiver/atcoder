import sys, math

X, A, D, N = map(int, input().split())

if D == 0:
    print(abs(X-A))
    sys.exit()

if D < 0:
    A = A + (N-1)*D
    D = -D

if X < A:
    print(A-X)
    sys.exit()

if X > A + (N-1)*D:
    print(X - (A+(N-1)*D))
    sys.exit()

i = math.floor((X-A)/D)
X_left = A + i*D
X_right = A + (i+1)*D

print(min(X-X_left, X_right-X))



