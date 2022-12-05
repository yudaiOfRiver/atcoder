N, M, Q = map(int, input().split())

points = [['No'] * N for _ in range(N)]
for _ in range(M):
    Ai, Bi, Ci = map(int, input().split())
    points[Ai][Bi] = Ci
    points[Bi][Bi] = -Ci

def maxPoint(Xi, Yi, p):
    if Xi == Yi:
        return p

    for next in N:
        if Xi != next and points[Xi][next] != 'No':
            p += points[Xi][next]
            res = max(res, maxPoint(next, Yi, p))
            return res



