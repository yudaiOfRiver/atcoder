N, A, B = map(int, input().split())

res = ""
hash = {0:".", 1:"#"}
for i in range(N):
    for j in range(N):
        c = (i+j) % 2
        for _ in range(B):
            res += hash[c]
    for _ in range(A):
        print(*res)
    res = ""

