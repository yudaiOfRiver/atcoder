import sys
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dict = defaultdict(set)
for Ai in A:
    dict[Ai].add(0)
for Bi in B:
    dict[Bi].add(1)

#print(dict)
for value in dict.values():
    if len(value) == 2:
        print(0)
        sys.exit()

res = float('inf')
A_and_B = sorted(dict.keys())
curNum, curSet = A_and_B[0], dict[A_and_B[0]]

for n in A_and_B:
    #print(curNum, n)
    if curSet == dict[n]:
        curNum = n
    else:
        res = min(res, n-curNum)
        curNum, curSet = n, dict[n]
    #print(res)

print(res)



