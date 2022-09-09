N = int(input())
P = [-1] + list(map(int, input().split()))

Q = [-1] + [0] * N
for i in range(1, N+1):
    pi = P[i]
    Q[pi] = i

print(*Q[1:])
