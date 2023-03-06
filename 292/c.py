import io
import sys
_INPUT = """\
19876
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#
N = int(input())

def divisor_list_s(num): # 約数の個数　
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 1
            if i**2 == num:
                continue
            count += 1
    return count

res = 0
for i in range(1, (N//2)+1):
    i_cnt = divisor_list_s(i)
    N_i_cnt = divisor_list_s(N-i)
#    print(i_cnt, N_i_cnt)
    if N % 2 == 0 and i == N//2:
        res += i_cnt * N_i_cnt
    else:
        res += 2 * i_cnt * N_i_cnt
#    print(res)

print(res)
