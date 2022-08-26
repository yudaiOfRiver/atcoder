def findThree(pos, n):
    index = 0
    for i in range(len(pos)):
        if pos[i] != 0:
            index += 1
        if index == n:
            return i

#pos = [0,0,0,3,4,1]
#print(findThree(pos))


N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

pos = [0 for _ in range(N)]

for i in range(K):
    pos[A[i]-1] = i+1
#print(pos)

for i in range(Q):
    index = findThree(pos, L[i])
    #print(index)
    if index+1 == len(pos):
        continue
    else:
        if pos[index+1] == 0:
            pos[index+1], pos[index] = pos[index], 0
    #print(pos)

for i in range(1, K+1):
    print(pos.index(i)+1, end=" ")


