import sys
S = input()

if S[0] != S[1]:
    if S[0] != S[2]:
        print(S[0])
    else:
        print(S[1])
    sys.exit()
if S[1] != S[2]:
    print(S[2])
    sys.exit()
print(-1)

