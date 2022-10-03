N, Q = map(int, input().split())
L = []
a = []

for _ in range(N):
    la = list(map(int, input().split()))
    li = la[0]
    L.append(li)
    ai = la[1:]
    a.append(ai)
# print(L)
# print(a)


s, t = [], []
for _ in range(Q):
    sk, tk = map(int, input().split())
    s.append(sk-1)
    t.append(tk-1)
# print(s)
# print(t)

for k in range(Q):
    sk, tk = s[k], t[k]
    print(a[sk][tk])
