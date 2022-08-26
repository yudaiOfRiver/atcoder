N, A, B = map(int, input().split())

field = [["."] * (N * B) for _ in range(N*A)]

for i in range(N*A):
    for j in range(N*B):
        if ((i // A) + (j // B))  % 2 == 1:
            field[i][j] = "#"

for i in range(N*A):
   print(*field[i])
