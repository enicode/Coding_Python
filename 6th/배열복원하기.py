# B[i][j] = A[i][j] + A[i-x][j-y] if x>X, y>Y 이므로,
# A[i][j] = B[i][j] - A[i-x][j-y] if x>X, y>Y

import sys
sys.stdin = open("6th\\input","r")

h,w,x,y = map(int, sys.stdin.readline().split())
matB = []
# 우선 겹쳐진 행렬을 그대로 다 저장한다.
for _ in range(h+x):
    matB.append(list(map(int, sys.stdin.readline().split())))
# 원래 행렬의 모습을 저장할 배열
matA = [[0 for i in range(w)] for j in range(h)]
# 위에서 부터 그리고 왼쪽부터 시작하므로 겹치지 않는 영역부터 우선 확인이 가능하므로, 
# 겹치지 않는 영역에서 matA를 부분적으로 만들고 이 부분을 이용하면서 겹치는 부분에서 matA 값을 다시 찾는다
for i in range(h):
    for j in range(w):
        # 겹치지 않는 영역의 행렬에 대해서는
        if i < x or j < y:
            # 그대로 값을 집어 넣고 출력한다.
            matA[i][j] = matB[i][j]
            print(matB[i][j], end = " ")
            continue
        # 겹치는 영역 대해서는 1~2번째 줄의 설명과 같이 값을 집어넣고 출력한다.
        matA[i][j] = matB[i][j]-matA[i-x][j-y]
        print(matB[i][j]-matA[i-x][j-y], end = " ")
    print()