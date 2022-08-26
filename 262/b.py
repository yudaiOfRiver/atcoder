# TLE

N, M = map(int, input().split())
uv = []
for _ in range(M):
    u, v = map(int, input().split())
    uv.append((u, v))

#print(uv)
seen = []
res = 0
for u1, v1 in uv:
    for u2, v2 in uv:
        if (u1, v1) == (u2, v2):
            break
        #print(u1, v1, u2, v2)
        if u1 == u2 and (((v1, v2) in uv) or ((v2, v1) in uv)):
            res += 1
        if u1 == v2 and (((u2, v1) in uv) or ((v1, u2) in uv)):
            res += 1
        if v1 == u2 and (((u1, v2) in uv) or ((v2, u1) in uv)):
            res += 1
        if v1 == v2 and (((u2, u1) in uv) or ((u1, u2) in uv)):
            res += 1
        #print("res", res)
res /= 3
res = int(res)
print(res)




#res = 0
#for i in range(N+1):
#    for j in range(i+1, N+1):
#        for k in range(j+1, N+1):
#            #print(i, j, k)
#            if ((i, j) in uv or (j, i) in uv) and ((j, k) in uv or (k, j) in uv) and ((k, i) in uv or (i, k) in uv):
#                res += 1

#print(res)


