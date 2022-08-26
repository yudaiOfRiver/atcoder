import numpy as np
import sys

H1, W1 = map(int, input().split())
A = []
for _ in range(H1):
    Ai = list(map(int, input().split()))
    A.append(Ai)

H2, W2 = map(int, input().split())
B = []
for _ in range(H2):
    Bi = list(map(int, input().split()))
    B.append(Bi)

B = np.array(B)

#H1, W1 = 4, 5
#A = np.array([[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
#H2, W2 =2,3
#B = np.array([[6,8,9], [16,18,19]])



for rows in range(1<<H1):  # 1: 削除、0:残す
    A_tmp = np.array(A.copy())
    for cols in range(1<<W1):
        rows_digits = '0' + str(H1) + 'b'
        rows_bin = format(rows,rows_digits)
        cols_digits = '0' + str(W1) + 'b'
        cols_bin = format(cols, cols_digits)

        if not (rows_bin.count('0') == H2 and cols_bin.count('0') == W2):
            continue

        A_tmp = np.array(A.copy())

        del_rows = []
        del_cols = []
        for i in range(H1):
            if rows & (1<<i):
                del_rows.append(i)

        for j in range(W1):
            if cols & (1<<j):
                del_cols.append(j)

        #print(del_rows, del_cols)

        A_tmp = np.delete(A_tmp, del_rows, axis=0)
        A_tmp = np.delete(A_tmp, del_cols, axis=1)

        #print(A_tmp)
        #print("-----")

        if np.array_equal(A_tmp, B):
            print("Yes")
            sys.exit()

print("No")






