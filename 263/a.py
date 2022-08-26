from collections import defaultdict
import sys

cards = map(int, input().split())

dict = defaultdict(lambda: 0)

for c in cards:
    dict[c] += 1

if len(dict) != 2:
    print("No")
    sys.exit()

val = list(dict.values())

if val[0] == 2 and val[1] == 3:
    print("Yes")
elif val[0] == 3 and val[1] == 2:
    print("Yes")
else:
    print("No")
