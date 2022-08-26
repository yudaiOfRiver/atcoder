from collections import Counter

N = int(input())
d = []
for _ in range(N):
    di = int(input())
    d.append(di)


c = Counter(d)
print(len(c))
