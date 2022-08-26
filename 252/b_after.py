import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mostDeliciousFoods = set()  # set of indices
curMax = 0

for i in range(N):
    if A[i] > curMax:
        curMax = A[i]
        mostDeliciousFoods.clear()
        mostDeliciousFoods.add(i+1)
    elif A[i] == curMax:
        mostDeliciousFoods.add(i+1)
    #print(mostDeliciousFoods)

for j in range(K):
    if B[j] in mostDeliciousFoods:
        print("Yes")
        sys.exit()

print("No")

