R, C = map(int, input().split())

R = abs(R-8)
C = abs(C-8)

higher = max(R, C)


if higher % 2 == 1:
    print("black")
else:
    print("white")







