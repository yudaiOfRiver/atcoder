N = int(input())
P = [-1] + [-1] + list(map(int, input().split()))

par = P[-1]
res = 1
while par != 1:
    #print(par)
    par = P[par]
    res += 1

print(res)



