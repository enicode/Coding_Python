# 아기상어의 먹이가 왼쪽 위에서 부터 결정하면 되므로, 단순하게 배열을 순서대로 검색 -> 가장 멀리있는 먹이부터 검색하게 되어 시간초과
# 아기상어의 먹이를 가까운순으로 검색하여 시간을 줄인다. => 마름모 꼴을 확장하는 식으로 검색 범위를 늘려나간다.

import sys
from collections import deque
sys.stdin = open('8th\\input','r')
N = int(sys.stdin.readline())
INF = float('inf')
# 상어의 크기에 대한 정보를 담을 변수 v[0]는 현재 크기고, v[1]은 현재 먹이를 먹은 횟수이다.
global v
v =[2,0]
# 현재까지 걸린 시간
global t
t = 0
# 현재 상어의 위치
global s
fishbowl=[]
#상어가 다음 먹이를 검색할 마름모(가장 위에서 부터 내려오면서 왼쪽 오른쪽 순서로 담는다.)
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
# 상어의 위치를 찾고, 어항상태를 받는다.
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(len(tmp)):
        if tmp[j] == 9:
            s = [i,j]
    fishbowl.append(tmp)
# 상어가 다음 시간 후에 먹이를 찾는다고 알려주는 함수.
def time():
    # 시간
    global t
    # 상어의 위치
    global s
    # 상어의 크기
    global v
    # 최대 361칸만 이동가능 한데 귀찮으니까 400
    d = 400
    # 상어의 다음 위치를 임시로 저장할 변수
    s_tmp = s
    # 마름모를 순서대로 검색하면 위에서부터 또한 왼쪽에서 부터 검색된다.(만들 때 그렇게 만듬)
    for point in next_point:
        # 만약 중간에 장애물이 없다고 가정할때 먹이까지 도달하는 최단거리가 현재 찾은 최단거리보다 길다면 탐색을 멈춘다.
        if abs(point[0])+abs(point[1]) > d : break
        # 먹이의 임시 위치
        f_tmp = [s[0]-point[0],s[1]+point[1]]
        # 경계 확인
        if f_tmp[0] < 0 or f_tmp[1] < 0 or f_tmp[0] > len(fishbowl)-1 or f_tmp[1] > len(fishbowl)-1:
            continue
        # 먹이가 상어의 크기보다 작고, 빈 곳이 아니라면, 가능성이 있으므로
        if fishbowl[f_tmp[0]][f_tmp[1]] < v[0] and fishbowl[f_tmp[0]][f_tmp[1]] > 0:
            # 먹이까지 거리의 임시 값
            d_tmp = dist(s, f_tmp)
            # 가장 가까운 먹이로 갱신
            if d_tmp < d:
                d = d_tmp
                # 먹이의 위치가 다음 상어의 위치가 될테니까
                s_tmp = f_tmp
    # 먹이를 찾을수 있었다면, <- d 값이 바뀌엇다면 
    if d < 400:
        # 상어는 이동할것이므로, 상어 위치를 0으로 바꾸고 <- 사실 처음에만 필요한 것
        fishbowl[s[0]][s[1]] = 0
        # 상어의 위치는 다음 위치로
        s = s_tmp 
        fishbowl[s[0]][s[1]] = 0
        # 이동거리만큼 시간이 증가                 
        t += d
        # 상어가 먹이를 먹었으므로, 상어가 먹은 횟수를 1증가시킨다.
        v[1] += 1
        # 만약 상어가 먹이를 먹은 횟수가 상어의 크기와 같아지면 상어의 크기를 1증가시키고, 먹은 횟수는 초기화 한다.
        if v[1] >= v[0]:
            v[0] += 1
            v[1] = 0
    else:
        # 먹이를 못찼았으므로 엄마상어를 찾으러 간다.
        print(t)
        sys.exit(0)
# 상어 위치와 먹이 위치를 주면 거리(시간)을 알려주는 BFS 함수
def dist(sp,fp):
    global v
    q = deque([])
    q.append(sp)
    # 방문안한곳 -1 로 초기화<- 이 배열에는 상어의 위치에서 그 위치까지 갈 때 필요한 이동거리가 담길텐데, 초기값이 0 이어야 하므로 -1로 초기화
    visited = [[-1 for i in range(N)] for j in range(N)]
    # 초기값 방문
    visited[sp[0]][sp[1]] = 0
    while q:
        # deque 앞에서 부터 꺼낸다. <- 한 위치까지 도달하는 방법은 최대 4가지가 있는데 그중에서 가장 거리가 짧은 것을 선택해야하므로, 
        # 거리가 짧은 곳에서부터 먼곳으로 확장하는 형식으로 되도록 선입선출로 한다.
        y,x = q.popleft()
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경계
            if nx<0 or ny<0 or ny>len(fishbowl)-1 or nx>len(fishbowl[ny])-1:
                continue
            # 만약 통과 가능하고(크기가 같아도 통과 가능), 방문한적이 없는 길이라면 다음 방문지로 한다.
            if fishbowl[ny][nx] <= v[0] and visited[ny][nx] == -1:
                # 다음 방문할 곳은 현재 방문한 곳에서 한칸 이동한 곳이므로, 1만큼 증가한 값을 저장한다.
                visited[ny][nx] = visited[y][x] + 1
                # 다음 방문할 곳이 먹이가 있는 곳이라면
                if [ny,nx] == fp:
                    # 먹이까지 거리를 반환한다.
                    return visited[ny][nx]
                #deque에 추가한다.
                q.append([ny,nx])   
    return INF
            
while True:
    time()