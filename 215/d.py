def make_divisor(N):
    sq_N = int(N**0.5)
    lower_divisor = []
    upper_divisor = []

    for i in range(1, sq_N+1):
        print("i", i)
        if N % i == 0:
            lower_divisor.append(i)
            if N//i != i:
                upper_divisor.append(N//i)

    divisor = lower_divisor + upper_divisor[::-1]
    return divisor


#N, M = map(int, input().split())
#A = list(map(int, input().split()))
N, M = 3, 12
A = [6, 1, 5]

devisors = set()

for i in range(N):
    devs_i = set(make_divisor(A[i]))
    devisors = devisors | devs_i

is_ans = [False] * (M+1)
for devi in range(len(devisors)):
    cur = devi
    while cur <= M:
        is_ans = True
        cur += devi


for i in range(1, M+1):
    if is_ans[i] == True:
        print(i)



