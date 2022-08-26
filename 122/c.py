N, Q = map(int, input().split())
S = input()

ACsUntil = [0]
cur = 0
for i in range(len(S)):
    if i != 0 and S[i-1] + S[i] == "AC":
        cur += 1
    ACsUntil.append(cur)

#print(ACsUntil)

for _ in range(Q):
    l, r = map(int, input().split())
    print(ACsUntil[r]-ACsUntil[l])



