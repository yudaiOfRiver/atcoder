N = int(input())


res = 0
while N // 2 >= 1:
    N = N // 2
    res += 1

print(res)
