H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

rows = len(S)
cols = len(S[0])

pos = []
for row in range(rows):
    for col in range(cols):
        if S[row][col] == "o":
            pos.append([row, col])

res = abs(pos[0][0]-pos[1][0]) + abs(pos[0][1]-pos[1][1])
print(res)
