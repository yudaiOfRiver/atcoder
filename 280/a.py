H, W = map(int, input().split())

res = 0
for _ in range(H):
    Si = input()
    for j in range(W):
        if Si[j] == '#':
            res += 1
print(res)




