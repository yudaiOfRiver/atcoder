s = input()

num = 1
tmp = s[0]
res = ""
for i in range(1, len(s)):
#    print(num, s[i], tmp)
    if s[i] == tmp:
        num += 1
    else:
        res += tmp + str(num)
        num = 1

    if i == len(s)-1:
        if s[i] == tmp:
            res += tmp + str(num)
        else:
            res += s[i] + '1'
    tmp = s[i]


print(res)


