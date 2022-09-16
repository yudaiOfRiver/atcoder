import sys

S = input()
T = input()

for i in range(len(S)+1):
#    print(T[:i])
    if S == T[:i]:
        print("Yes")
        sys.exit()

print("No")
