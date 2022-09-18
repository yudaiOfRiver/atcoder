N = int(input())

XY = []
for i in range(N):
    Xi, Yi = map(int, input().split())
    XY.append((Xi, Yi))

# N = 6
# XY = [(-1, -1), (0, 1),(0, 2),(1, 0),(1, 2),(2, 0)]

# XY =[(2, 1),(2, -1),(1, 0),(3, 1),(1, -1)]


def dfs(x, y):
    directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
    for xi, yi in directions:
        X, Y = x+xi,y+yi
        if (X, Y) not in seen and (X,Y) in XY:
            seen.add((X, Y))
            dfs(X, Y)

seen = set()
res = 0
for xi, yi in XY:
    if (xi, yi) not in seen:
        seen.add((xi, yi))
        dfs(xi, yi)
        res += 1
print(res)
