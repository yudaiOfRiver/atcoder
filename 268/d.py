from itertools import combinations_with_replacement, permutations
import sys

N, M = map(int, input().split())

S = []
T = []

for i in range(N):
   si = input()
   S.append(si)
for i in range(M):
   ti = input()
   T.append(ti)

# N, M = 2, 2
# S = ["choku", "dai"]
# T = ["chokudai", "choku_dai"]

S_joined = "".join(S)
leftnum = 16 - len(S_joined)

for v in permutations(range(N), N):  # Siの組合せを全探索

    for cr in combinations_with_replacement(range(N-1), leftnum-(N-1)):  # "_" の配置を全探索
        intervals = [1] * (N-1)
        for cri in cr:
            intervals[cri] += 1

        res = ""
        print(v)
        print(intervals)
        for vi, cri in enumerate(list(v), intervals):
            res += S[vi]
            res += "_" * cri
        res += S[list(v)[-1]]

        if res not in T:
            print(res)
            sys.exit()

print(-1)


