# 폭탄 마다 카운트들 달아서 터질지 안터질지 체크

import sys

r, c, n = map(int, sys.stdin.readline().split())

board = [[] for _ in range(r)]

for i in range(r):
    tmp_str = sys.stdin.readline()
    for j in range(c):
        if tmp_str[j] == "O":
            #폭탄에는 타이머를 단다.
            board[i].append([tmp_str[j],3])
        else:
            board[i].append(tmp_str[j])
# 매초 마다 다음과 같은 확인을 한다.    
for i in range(1, n+1):
    #만약 폭탄이라면 타이머를 1 감소시킨다.
    for j in range(r):
        for k in range(c):
            if board[j][k][0] == "O":
                board[j][k][1] -= 1
    # 그리고 난뒤
    for j in range(r):
        for k in range(c):
            # 타이머가 0 인 폭탄이 있으면 터트린다. 
            if board[j][k][0] == "O" and board[j][k][1] == 0:
                board[j][k] = "."
                # 주위도 빈공간으로 한다. 단, 자기와 같은 순간 터질 폭탄이 있다면 지우지 않는다.
                if j+1 < r and board[j+1][k][0] == "O" and board[j+1][k][1] != 0:
                    board[j+1][k] = "."
                if j-1 >= 0:
                    board[j-1][k] = "."
                if k+1 < c and board[j][k+1][0] == "O" and board[j][k+1][1] != 0:
                    board[j][k+1] = "."
                if k-1 >= 0:
                    board[j][k-1] = "."
    # 짝수초 마다 빈 공간에 폭탄을 설치한다.
    if i%2 == 0:
        for j in range(r):
            for k in range(c):
                if board[j][k] == ".":
                    board[j][k] = ["O",3]

for line in board:
    for space in line:
        print(space[0], end="")
    print()
                