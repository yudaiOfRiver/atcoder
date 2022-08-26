N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

for i in range(N):
    next = (i+1)%N
    T[next] = min(T[next], S[i]+T[i])
    #print(T)
#print("=======")
for i in range(N):
    next = (i+1)%N
    T[next] = min(T[next], S[i]+T[i])
    #print(T)

for i in range(N):
    print(T[i])
