from collections import Counter

c = Counter(list(input().split()))
#print(c)

pair = list(c.values())
pair.sort()
#print(pair)

if pair == [2, 3]:
    print("Yes")
else:
    print("No")


