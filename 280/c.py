S = input()
T = input()

res = 0
while res < len(S):
    if S[res] == T[res]:
        res += 1
    else:
        break
print(res+1)



