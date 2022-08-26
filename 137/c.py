from collections import Counter


N = int(input())
s = []
for _ in range(N):
    si = input()
    s.append(si)


#anagrams = defau

for i in range(N):
    s[i] = "".join(sorted(s[i]))

c = Counter(s)
#print(c)

res = 0
for val in c.values():
    if val > 1:
        res += (val*(val-1))//2

print(res)




