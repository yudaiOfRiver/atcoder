import sys

N = int(input())
a = list(map(int, input().split()))
sum = len(a)
a = set(a)
#print(a)

if N == 1:
    if 1 in a:
        print(1)
        sys.exit()
    else:
        print(0)
        sys.exit()


res = 0
while sum >= 0:
#    print(res, sum)
    res += 1
    if res in a:
        sum -= 1
    else:
        sum -= 2

print(res-1)



