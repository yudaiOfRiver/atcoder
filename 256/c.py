h1, h2, h3, w1, w2, w3 = map(int, input().split())

res = 0
#r1 = [[0]*3]
candi1 = []
candi2 = []


for i11 in range(1, 29):
    for i12 in range(1, 29):
        if i11 + i12 > h1 - 1:
            continue
        candi1.append([i11, i12, h1-i11-i12])

for i21 in range(1, 29):
    for i22 in range(1, 29):
        if i21 + i22 > h2 - 1:
            continue
        candi2.append([i21, i22, h2-i21-i22])

for ca1 in candi1:
    for ca2 in candi2:
        if ca1[0] + ca2[0] > w1 - 1 or ca1[1] + ca2[1] > w2 - 1 or ca1[2] + ca2[2] > w3 - 1:
            continue

        i13 = w1 - ca1[0] - ca2[0]
        i23 = w2 - ca1[1] - ca2[1]
        i33 = w3 - ca1[2] - ca2[2]
        if i13 + i23 + i33 == h3:
            res += 1

print(res)




