H, W = map(int, input().split())
R, C = map(int, input().split())

adj = [[R+1, C], [R-1, C], [R, C+1], [R, C-1]]

res = 0
for i, j in adj:
    if i in range(1, H+1) and j in range(1, W+1):
        res += 1
print(res)

