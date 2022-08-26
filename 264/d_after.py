S = input()

dict = {"a": 1, "t":2, "c":3, "o":4, "d":5, "e":6, "r":7}

N = []
for Si in S:
    N.append(dict[Si])

res = 0
for i in range(len(N)):
    for j in range(i):
        if N[i] < N[j]:
            res += 1

print(res)

