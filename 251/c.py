N = int(input())

submitted = set()
curMax = 0
res = 0

for i in range(N):
    si, ti = input().split()
    ti = int(ti)

    if si not in submitted:
        submitted.add(si)
        if ti > curMax:
            res = i+1
            curMax = ti

print(res)

