N = int(input())
a = list(map(int, input().split()))
a = [-1] + a # 1-index

seen = set()
res = 0
same = 0
for i in range(1, N+1):
    #print("i", i)
    if i == a[i]:
        same += 1
    else:
        k = a[i]
        if a[k] == i and k not in seen:
            res += 1
            seen.add(i)
            seen.add(k)
    #print("res", res)
    #print("same", same)
    #print("=====")
res += same*(same-1)/2
res = int(res)
print(res)


