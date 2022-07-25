import sys
from collections import deque
sys.stdin = open('8th\\input','r')
N = int(sys.stdin.readline())
INF = float('inf')
global v
v =[2,0]
global t
t = 0
global s
fishbowl=[]
#상어가 다음 먹이를 검색할 마름모
next_point = []
for i in range(1,2*N-1):
    tmp =[]
    for j in range(i,-i-1,-1):
        if abs(j) == abs(i):
            tmp.append((j,0))
        elif j > 0:
            tmp.append((j,-(i-j)))
            tmp.append((j,i-j))
        else:
            tmp.append((j,-i-j))
            tmp.append((j,i+j))
    next_point.extend(tmp)
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(len(tmp)):
        if tmp[j] == 9:
            s = [i,j]
    fishbowl.append(tmp)
# 상어가 다음 먹이를 먹는 함수
def time():
    global t
    global s
    global v
    d = 400
    s_tmp = s
    for point in next_point:
        if abs(point[0])+abs(point[1]) > d : break
        f_tmp = [s[0]-point[0],s[1]+point[1]]
        if f_tmp[0] < 0 or f_tmp[1] < 0 or f_tmp[0] > len(fishbowl)-1 or f_tmp[1] > len(fishbowl)-1:
            continue
        if fishbowl[f_tmp[0]][f_tmp[1]] < v[0] and fishbowl[f_tmp[0]][f_tmp[1]] > 0:
            d_tmp = dist(s, f_tmp)
            if d_tmp < d:
                d = d_tmp
                s_tmp = f_tmp
    if d < 400:
        fishbowl[s[0]][s[1]] = 0
        s = s_tmp 
        fishbowl[s[0]][s[1]] = 0                 
        t += d
        v[1] += 1
        if v[1] >= v[0]:
            v[0] += 1
            v[1] = 0
    else:
        print(t)
        sys.exit(0)
# 상어와 먹이 사이의 거리(시간)을 알려주는 함수.
def dist(sp,fp):
    global v
    q = deque([])
    q.append(sp)
    visited = [[-1 for i in range(N)] for j in range(N)]
    visited[sp[0]][sp[1]] = 0
    while q:
        y,x = q.popleft()
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or ny>len(fishbowl)-1 or nx>len(fishbowl[ny])-1:
                continue
            if fishbowl[ny][nx] <= v[0] and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                if [ny,nx] == fp:
                    return visited[ny][nx]
                q.append([ny,nx])   
    return INF
            
while True:
    time()