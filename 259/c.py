import sys
from itertools import groupby

S = input()
T = input()

# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


S_rl = runLengthEncode(S)
T_rl = runLengthEncode(T)

if len(S_rl) != len(T_rl):
    print("No")
    sys.exit()

for s_rl, t_rl in zip(S_rl, T_rl):
    #print(s_rl, t_rl)
    if s_rl[0] != t_rl[0]:
        print("No")
        sys.exit()
    else:
        if (s_rl[1] == 1 and t_rl[1] != 1) or (s_rl[1] != 1 and t_rl[1] == 1) or (s_rl[1] > t_rl[1]):
            print("No")
            sys.exit()

print("Yes")








