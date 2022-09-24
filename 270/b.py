X, Y, Z = map(int, input().split())

def my_sign(x):
    return (x > 0)

if (my_sign(X) != my_sign(Y)) or (abs(X) < abs(Y)):
    print(abs(X))
elif (my_sign(Y) != my_sign(Z)):
    print(abs(X)+2*abs(Z))
elif (abs(Z) < abs(Y)):
    print(abs(X))
else:
    print(-1)

