N, M = map(int, input().split())

k = []
s = []
for _ in range(M):
    ki, *si = map(int, input().split())
    k.append(ki)
    s.append(si)
#print(k)
#print(s)

p = list(map(int, input().split()))

res = 0
for bit in range(1<<N):
    for i in range(M):
        on_switch = 0

        for siki in range(N):
            if bit>>i & 1 and siki in s[i]:
                on_switch += 1

        if on_switch % 2 != p[i]:
            break
    else:
        res += 1
print(res)

