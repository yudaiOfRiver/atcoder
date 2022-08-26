N = int(input())

A = []
for i in range(N):
    temp = A
    A = []
    for j in range(i+1):
        if j == 0 or j == i:
            A.append(1)
        else:
            aij = temp[j-1] + temp[j]
            A.append(aij)
    print(*A)
#print(*A)
