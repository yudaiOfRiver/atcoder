N = int(input())
a = [-1] + list(map(int, input().split()))

same = 0
for i in range(1, N+1):
    if a[i] == i:
        same += 1

cnt = 0
for i in range(1, N+1):
    if i != a[i]:
        j = a[i]
        if a[j] == i:
            cnt += 1
cnt = cnt // 2
cnt += same * (same-1) // 2
print(cnt)


