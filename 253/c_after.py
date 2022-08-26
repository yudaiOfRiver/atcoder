from collections import OrderedDict

Q = int(input())

od = OrderedDict()

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        od[x]
    elif query[0] == 2:
        x, c = query[1], query[2]
        del_num = min(c, S.count(x))
        for _ in range(del_num):
            S.remove(x)
    else:
        max_num, min_num = max(S), min(S)
        print(max_num - min_num)



