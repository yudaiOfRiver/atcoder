from os import set_blocking


N = int(input())

N_bin = bin(N)[2:]



subsets = set()
subsets.add(N_bin)
for i in range(len(N_bin)):
    if N_bin[i] == '1':
        sub_tmp = subsets.copy()
        for sub in sub_tmp:
            subset = sub[:i] + '0' + N_bin[i+1:]
            subsets.add(subset)

new = []
for subset in subsets:
    new.append(int(subset, 2))

new.sort()
for i in new:
    print(i)


