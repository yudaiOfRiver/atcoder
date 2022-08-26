H, W = map(int, input().split())
R, C = map(int, input().split())

if H in range(1, 3) and W in range(1, 3):
    print(H+W-2)
elif (H in range(1, 3) and W not in range(1, 3)):
    if C == 1 or C == W:
        print(H)
    else:
        print(H+1)
elif (W in range(1, 3) and H not in range(1, 3)):
    if R == 1 or R == H:
        print(W)
    else:
        print(W+1)
else:
    if (R==1 or R==H) and (C in range(2, W)):
        print(3)
    elif (C==1 or C==W) and (R in range(2, H)):
        print(3)
    elif (R==1 or R==H) and (C==1 or C==W):
        print(2)
    else:
        print(4)
