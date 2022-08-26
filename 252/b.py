import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

likes = set()
curMax = 0

for i in range(N):
    if A[i] > curMax:
        likes.clear()
        likes.add(i)
        curMax = A[i]
    if A[i] == curMax:
        likes.add(i)

for j in range(K):
    if B[j] in likes:
        print("Yes")
        sys.exit()

print("No")
