# 1시간씩 진행시키면서 1이 모두 사라지는 경우에 N을 출력한다.
import sys
import copy
sys.stdin = open('8th\input','r')
N, M = map(int,sys.stdin.readline().split())

def check(p):
    envs = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        y, x = p
        y += dy[i]
        x += dx[i]
        if not check_board[y][x]:
            envs += 1
        if envs >= 2:
            return True
    return False

def env_cheese(p):
    q = []
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q.append(p)
    while True:
        oy, ox = q.pop()
        visited.append([oy,ox])
        for i in range(4):
            y, x = oy, ox
            y += dy[i]
            x += dx[i]
            if x < 0 or y < 0 or y > len(board)-1 or x > len(board[y]) - 1:
                continue
            if check_board[oy][ox] == 0 and board[y][x] == 0 and [y,x] not in visited:
                check_board[y][x] = 0   
                q.append([y,x])
        # 모두 돌았으면 종료
        if not q: return
    
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check_board = [[0 if i == 0 or i == M-1 or j == 0 or j == N-1 else 1 for i in range(M)] for j in range(N)] 
t = 0
visited = []
env_cheese([0,0])
while True:
    melt_c = []              
    for i in range(1,len(board)-1):
        for j in range(1,len(board[i])-1):
            if board[i][j] == 1 and check([i,j]):
                melt_c.append([i,j])
                
    if not melt_c:
        break
    for c in melt_c:
        board[c[0]][c[1]] = 0
    for c in melt_c:
        check_board[c[0]][c[1]] = 0
        env_cheese([c[0],c[1]])
    t += 1
print(t)  
    
    