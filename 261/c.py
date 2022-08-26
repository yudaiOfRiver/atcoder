from collections import defaultdict

N = int(input())

freq = defaultdict(lambda: 0)

for i in range(N):
    Si = input()
    if freq[Si] == 0:
        print(Si)
    else:
        num = freq[Si]
        print(Si + "(" + str(num) + ")")
    freq[Si] += 1
