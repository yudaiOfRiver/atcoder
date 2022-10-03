N = int(input())

n = hex(N)[2:]
res = ''
strings = ['a', 'b', 'c', 'd', 'e', 'f']
for ni in n:
    if ni in strings:
        res +=  str.upper(ni)
    else:
        res += ni

if len(res) == 1:
    res = '0' + res

print(res)
