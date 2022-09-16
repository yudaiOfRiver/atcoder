N = int(input())
S = input()

res = 1
tmp = S[0]
for i in range(1, N):
    if tmp == S[i]:
        continue
    else:
        res += 1
    tmp = S[i]

print(res)

