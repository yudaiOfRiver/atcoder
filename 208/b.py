import math

P = int(input())

res = 0
for i in range(10, -1, -1):
    a = math.factorial(i)
    res += (P // a)
    P = P % a
    print(i, P, res)
print(res)


