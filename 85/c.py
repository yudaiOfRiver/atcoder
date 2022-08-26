import sys

N, Y = map(int, input().split())

max_man = Y // 10000

for i in range(max_man+1):
    max_gosen = (Y - 10000*i) // 5000
    for j in range(max_gosen+1):
#        print("i", i)
#        print("j", j)
        if 10000 * i + 5000 * j + 1000 * (N-i-j) == Y:
            print(i, j, N-i-j)
            sys.exit()

print(-1, -1, -1)
