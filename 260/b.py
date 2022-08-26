N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

info = [[] for _ in range(N)]
for i in range(N):
    info[i].append(i+1)
    info[i].append(A[i])
    info[i].append(B[i])


res = []
passer = set()

info1 = sorted(info, key=lambda x: x[1], reverse=True)
k = 0
while len(res) < X:
    if info1[k][0] not in passer:
        res.append(info1[k][0])
        passer.add(info1[k][0])
    k += 1
#print(res)
#print("1", info1)

info2 = sorted(info, key=lambda x: x[2], reverse=True)
k = 0
while len(res) < X+Y:
    if info2[k][0] not in passer:
        res.append(info2[k][0])
        passer.add(info2[k][0])
    k += 1
#print(res)
#print("2", info2)

info3 = sorted(info, key=lambda x: x[1]+x[2], reverse=True)

k = 0
while len(res) < X+Y+Z:
    if info3[k][0] not in passer:
        res.append(info3[k][0])
        passer.add(info3[k][0])
    k += 1
#print(res)
#print("3", info3)


res.sort()
for r in res:
    print(r)











