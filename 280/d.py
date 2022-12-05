from collections import Counter

K = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def legendre(N, p): # N! が p で何回割り切れるか
    if N < p:
        return 0
    return N//p + legendre(N//p, p)

def binarySearch(p, target) -> int:
    l, r = 0, 10**12
    N = (l+r) // 2
    while l < r:
        N = (l+r) // 2
#        print(l, N, r)
#        print(legendre(N, p))
        if legendre(N, p) < target:
            l = N + 1
        elif legendre(N, p) >= target:
            r = N
    return l


ele = prime_factorize(K)
ele_cnt = Counter(ele)
res = 0
for ele, cnt in ele_cnt.items():
    res = max(res, binarySearch(ele, cnt))

print(res)






