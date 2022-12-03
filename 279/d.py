from math import floor, ceil

A, B = map(int, input().split())


def calc(x):
    return A/((1+x)**(1/2)) + x*B

x = (A/(2*B))**(3/2) - 1
if x < 0:
    x = 0

print(x)
x_low, x_high = floor(x), ceil(x)
res = min(calc(x_low), calc(x_high))
print(res)

