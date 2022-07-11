# B[i][j] = A[i][j] + A[i-x][j-y] if x>X, y>Y 이므로,
# A[i][j] = B[i][j] - A[i-x][j-y] if x>X, y>Y

import sys
sys.stdin = open("6th\\input","r")

h,w,x,y = map(int, sys.stdin.readline().split())
matB = []
for _ in range(h+x):
    matB.append(list(map(int, sys.stdin.readline().split())))
matA = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        if i < x or j < y:
            matA[i][j] = matB[i][j]
            print(matB[i][j], end = " ")
            continue
        matA[i][j] = matB[i][j]-matA[i-x][j-y]
        print(matB[i][j]-matA[i-x][j-y], end = " ")
    print()