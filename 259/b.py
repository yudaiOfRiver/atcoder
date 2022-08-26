import math

a, b, d = map(int, input().split())

a_prime = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
b_prime = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))

print(a_prime, b_prime)

