import sys

N = int(input())
A = [input() for _ in range(N)]

dict = {'W': 'L', 'D': 'D', 'L': 'W'}

for i in range(1, N):
    for j in range(i):
        Aij = A[i][j]
        if dict[Aij] != A[j][i]:
            print('incorrect')
            sys.exit()

print('correct')
