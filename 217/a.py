import sys

S, T = input().split()
Sn = len(S)-1
Tn = len(T)-1

for i in range(10):
    if Sn < i:
        print("Yes")
        sys.exit()

    if Tn < i:
        print("No")
        sys.exit()

    if S[i] < T[i]:
        print("Yes")
        sys.exit()

    elif S[i] > T[i]:
        print("No")
        sys.exit()

