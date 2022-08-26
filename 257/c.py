import sys
from collections import defaultdict

N = int(input())
S = input()
W = list(map(int, input().split()))



#child = 0
#child_max, adult_min = 0, float('inf')
#for i in range(N):
#    if S[i] == 0:
#        child += 1
#        child_max = max(child_max, W[i])
#    else:
#        adult_min = min(adult_min, W[i])
#
#if child_max < adult_min:
#    print(N)
#    sys.exit()

child = 0
dict = defaultdict(list)
for i in range(N):
    dict[W[i]].append(S[i])
    if S[i] == '0':
        child += 1

#print(dict)
#print(child)

cost = N-child
res = 0
W.sort()
#print(len(dict))
for i in range(len(dict)):
    for j in range(len(dict[W[i]])):
        if dict[W[i]][j] == '0':
            cost += 1
        else:
            cost -= 1
        #print(W[i], j)
        #print(cost)
        res = max(res, cost)
print(res)







