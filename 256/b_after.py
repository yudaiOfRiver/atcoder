N = int(input())
A = list(map(int, input().split()))
A = A[::-1]

S = [0]
curSum = 0
for Ai in A:
    curSum += Ai
    S.append(curSum)

#print(S)
res = 0
for si in S:
    res += (si >= 4)
print(res)


