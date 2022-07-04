import sys

r, c, n = map(int, sys.stdin.readline().split())

board = [[] for _ in range(r)]

for i in range(r):
    tmp_str = sys.stdin.readline()
    for j in range(c):
        if tmp_str[j] == "O":
            board[i].append([tmp_str[j],3])
        else:
            board[i].append(tmp_str[j])
    
for i in range(1, n+1):
    for j in range(r):
        for k in range(c):
            if board[j][k][0] == "O":
                board[j][k][1] -= 1
    for j in range(r):
        for k in range(c):
            if board[j][k][0] == "O" and board[j][k][1] == 0:
                board[j][k] = "."
                if j+1 < r and board[j+1][k][0] == "O" and board[j+1][k][1] != 0:
                    board[j+1][k] = "."
                if j-1 >= 0:
                    board[j-1][k] = "."
                if k+1 < c and board[j][k+1][0] == "O" and board[j][k+1][1] != 0:
                    board[j][k+1] = "."
                if k-1 >= 0:
                    board[j][k-1] = "."
    if i%2 == 0:
        for j in range(r):
            for k in range(c):
                if board[j][k] == ".":
                    board[j][k] = ["O",3]

for line in board:
    for space in line:
        print(space[0], end="")
    print()
                