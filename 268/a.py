from collections import Counter

X = list(map(int, input().split()))

c = Counter(X)
print(len(c))
