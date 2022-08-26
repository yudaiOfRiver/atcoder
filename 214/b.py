S, T = map(int, input().split())

res = 0

for a in range(S+1):
    for b in range(S-a+1):
        for c in range(S-a-b+1):
            #print(a, b, c)
            if a + b + c <= S and a * b * c <= T:
                res += 1
print(res)



