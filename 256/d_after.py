N = int(input())
intervals = [
    list(map(int, input().split()))
    for _ in range(N)
]
intervals.sort()

res = []
for l, r in intervals:
    #print(l,r, res)
    if res == []:
        res.append([l, r])
    else:
        if l <= res[-1][1]:
            res[-1][1] = max(res[-1][1], r)
        else:
            res.append([l, r])
#print(res)

for l,r in res:
    print(l, r)




