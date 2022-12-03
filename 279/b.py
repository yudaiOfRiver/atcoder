import sys

S = input()
T = input()

total = len(S) - len(T) + 1
for i in range(total):
    if T == S[i:i+len(T)]:
        print("Yes")
        sys.exit()
print("No")

