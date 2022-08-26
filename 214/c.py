#N = int(input())
#S = [-1] + list(map(int, input().split()))
#T = [-1] + list(map(int, input().split()))

N = 3
S = [-1, 4, 1, 5]
T = [-1, 3, 10, 100]

t = 1
have = [-1] + [0] * N
res = [-1] + [10**10] * N
while any(resi != 10**10 for resi in res):
    print("t", t)
    for i in range(1, N+1):
        if t == T[i]:
            have[i] += 1
            res[i] = min(res[i], t)
            print("have\n",have)
    for i in range(1, N+1):
        if t % S[i] == T[i]:
            have[(i+1)//N] += 1
            have[i] -= 1
            print("have\n", have)
    print('==')
    if t == 20:
        break
    t += 1


for i in range(1, N+1):
    print(res[i])
