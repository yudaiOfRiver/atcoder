N = int(input())
S = []
for _ in range(N):
    S.append(input())


time = [0 for _ in range(10)]
deltaT = 1

for i in range(10):     # loop for number displayed
    deltaT = 1
    for j in range(1,11):    # loop for Si
        for k in range(N):       # loop for number slot
            if str(i) == S[k][j % 10]:
                time[i] += deltaT
                deltaT = 1
                break
        deltaT += 1


print(time)



