from collections import Counter

S = input()

c = Counter(S)
res = c['v'] + c['w'] * 2
print(res)
