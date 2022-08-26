import sys

X, A, D, N = map(int, input().split())

if D == 0:
    print(X-A)
    sys.exit()


if D > 0:
    if X >= A + (N-1)*D or X <= A:
        res = min(abs(X - (A + (N-1)*D)), abs(X-A))
        print(res)
        sys.exit()
    else:
        tmp = (X-A) % D
        res = min(tmp, abs(D-tmp))
        print(res)
        sys.exit()

if D < 0:
    if X >= A or X <= A + (N-1)*D:
        res = min(abs(X - (A + (N-1)*D)), abs(X-A))
        print(res)
        sys.exit()
    else:
        tmp = abs(X-A) % abs(D)
        res = min(tmp, abs(D)-tmp)
        print(res)
        sys.exit()





