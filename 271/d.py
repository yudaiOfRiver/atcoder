N, S = map(int, input().split())
a, b = [], []
for _ in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

DP = [[False] * (S+1) for _ in range(N+1)]


"""
1
1

1
2

5
2 3 4 4 9

5
1 1 2 2 3
"""
