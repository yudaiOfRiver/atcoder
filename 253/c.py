from collections import defaultdict, deque
Q = int(input())

min_queue = deque()
max_queue = deque()

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        max_queue.append(query[1])

    elif query[0] == 2:
        i = 0
        while queue.popleft() == query[1] or i == query[2]:
            i += 1
        S[query[1]] -= delete_num
    else:
        print(max_num - min_num)
    #print(max_num, min_num)
    #print(S)





