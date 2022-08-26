import math

N, X = map(int, input().split())

i = math.ceil(X/N)-1
#print(i)
i = i % 26
#print(i)
#print(str_i)

a_i = ord('A')
print(chr(a_i + i))
