from collections import defaultdict
N = int(input())

S = []
for _ in range(N):
    Si = input()
    S.append(Si)

minTime = float('inf')

for digit in range(10):
    time = float('inf')
    indices = defaultdict(lambda: 0)
    for n in range(N):
        index = S[n].index(str(digit))
        indices[index] += 1
    #print(indices)

    circuit = max(indices.values())
    if circuit == 1:
        time = max(indices.keys())
    else:
        max_index = 0    # max index in indices which has max overlap
        for index in indices.keys():
            if indices[index] == circuit:
                max_index = max(index, max_index)
                time = max_index + 10 * (circuit-1)
    #print(time)
    minTime = min(time, minTime)


print(minTime)





