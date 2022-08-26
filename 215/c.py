from itertools import permutations

S, K = input().split()
S = list(S)
S.sort()
K = int(K)
#print(S)

count = 1
seen = set()
for v in list(permutations(S)):
    if v in seen:
        continue
    if count == K:
        res = v
        break
    seen.add(v)
    count += 1

print("".join(res))





