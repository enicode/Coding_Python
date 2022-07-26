# 1시간씩 진행시키면서 1이 모두 사라지는 경우에 N을 출력한다.
import sys
from collections import deque
import copy
sys.stdin = open('8th\input','r')
N, M = map(int,sys.stdin.readline().split())

# 치즈가 외부공기로 둘러 쌓엿는지 알려주는 함수
def check(p,e):
    # 외부공기와 맞닿은 면의 갯수
    envs = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    y, x = p
    # 치즈의 4면의 상태를 확인하면서   
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 외부공기와 만나면 envs 1증가
        if not e[ny][nx]:
            envs += 1
        # envs 값이 2이상이면 True
        if envs >= 2:
            return True
    return False
# 외부와 연결된 공기를 표현한 environment를 수정할 BFS 함수, 외부공기인 p 위치부터 함수를 시작하여 외부공기를 확장한다.
def env(p):
    q = deque([])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q.append(p)
    environment[p[0]][p[1]] = 0
    while True:
        y, x = q.popleft()
        # 위치의 사방을 확인한다.
        for i in range(4):
            ny, nx = y, x
            ny += dy[i]
            nx += dx[i]
            # 경계
            if nx < 0 or ny < 0 or ny > len(board)-1 or nx > len(board[y-1]) - 1:
                continue
            # 방문할 위치가 공기이고, 방문한적 없는 곳이라면 
            if board[ny][nx] == 0 and environment[ny][nx]:
                # 방문할 위취를 외부공기로 표시하고 q 에 담는다.
                environment[ny][nx] = 0   
                q.append([ny,nx])
        # 모두 돌았으면 종료
        if not q: return    
board = []
cheeses =deque([]) 
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if tmp[j] == 1:
            cheeses.append([i,j])
    board.append(tmp)
 
# 시간
t = 0
# 외부공기를 0 그렇지 않은 영역은 1로 표현할 2차원 배열 초기는 1
environment = [[1 for i in range(M)] for j in range(N)]
# 외부 공기 초기화
env([0,0])
while cheeses:
    num_left_c = len(cheeses)
    melt_cheese = []
    # 치즈가 녹을지 안녹을지 확인한다.
    for i in range(num_left_c):
        cheese= cheeses.pop()
        if check(cheese,environment):
            melt_cheese.append(cheese)
        # 안녹을 치즈라면 다시 담는다.
        else:
            cheeses.appendleft(cheese)
    # 녹을 치즈들로 외부 공기를 갱신한다.
    for cheese in melt_cheese:
        env(cheese)
    t += 1
print(t)
'''
while True:
    original_environment = copy.deepcopy(environment)
    tmp_y_min, tmp_y_max = N-2, 1
    tmp_x_min, tmp_x_max = M-2, 1
    more_melt = False
    for i in range(y_min,y_max+1):
        for j in range(x_min,x_max+1):
            if board[i][j] == 1 and check([i+1,j+1], original_environment):
                board[i][j] = 0
                environment[i+1][j+1] = 0
                env([i+1,j+1])
                tmp_y, tmp_x = i, j
                if tmp_y > tmp_y_max:
                    tmp_y_max = tmp_y
                if tmp_y < tmp_y_min:
                    tmp_y_min = tmp_y
                if tmp_x > tmp_x_max:
                    tmp_x_max = tmp_x
                if tmp_x < tmp_x_min:
                    tmp_x_min = tmp_x
                more_melt = True
    if not more_melt:
        break
    t += 1                                  
    y_min, y_max, x_min, x_max = tmp_y_min, tmp_y_max, tmp_x_min, tmp_x_max
'''                