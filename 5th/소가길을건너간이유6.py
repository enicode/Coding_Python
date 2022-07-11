# BFS? 카카오 늑대와양과 비슷
# 1. 길을 건너서만 갈 수 있는 지역을 구분하고 그 안에 소가 몇마리 인지 센다.(둘이 동시에)
# 2. 고립된 지역에서 2곳을 뽑는다(모든 경우의 수), 지역 2곳의 소 숫자를 곱한다.
# 1-1 고립된 지역은 한 지역에서 길을 건너지 않고 지나갈 수있는 영역을 확장하는 식으로
import sys
from collections import deque
from itertools import combinations

# 목초지 하나가 들어오면 그 목초지를 기준으로 영역을 확장하여 길없이 다닐 수 있는 하나의 목초지로 확장
# 하나의 목초지로 확장된 목초지들 정보와, 그 때 목초지에 있는 소들의 숫자를 반환
def BFS(board, cow_info, root):
    visited = []
    q =deque([root])
    num_cows = 0
    while q:
        n =q.popleft()
        if n not in visited:
            visited.append(n)
            num_cows += cow_info[n[0]][n[1]]
            # pass는 보드 경계 때문에
            if n[0]-1< 0:
                pass
            else:
                # 길이 없고, 그 곳이 방문한 곳이 아닐때 하나의 목초지로 넣는다. 각 방향마다.
                if not board[n[0]][n[1]][0] and not [n[0]-1,n[1]] in visited:
                    q += [[n[0]-1,n[1]]]
            if n[1]-1 < 0 :
                pass
            else:
                if not board[n[0]][n[1]][3] and not [n[0],n[1]-1] in visited:
                    q += [[n[0],n[1]-1]]
            if n[0]+1 > len(board)-1 :
                pass
            else:
                if not board[n[0]][n[1]][2] and not [[n[0]+1,n[1]]] in visited:
                    q += [[n[0]+1,n[1]]]
            if n[1]+1 > len(board)-1 :
                pass
            else:
                if not board[n[0]][n[1]][1] and not [n[0],n[1]+1] in visited:
                    q += [[n[0],n[1]+1]]
                         
            
    return visited, num_cows

n,k,r = map(int, sys.stdin.readline().split())
# pasture[i][j] = [0,0,0,0] NESW 방향으로 길이 있음:1 길이 없음:0
pasture =[[[0,0,0,0]for i in range(n)] for j in range(n)]
cows = [[0 for i in range(n)] for j in range(n)]
for _ in range(r):
    tmp = list(map(int, sys.stdin.readline().split()))
    # 길로 연결된 두 목초지 사이의 관계를 나타낸다.
    if tmp[0]-tmp[2] > 0 :
        pasture[tmp[0]-1][tmp[1]-1][0] = 1
        pasture[tmp[2]-1][tmp[3]-1][2] = 1
    elif tmp[0]-tmp[2] < 0 :
        pasture[tmp[0]-1][tmp[1]-1][2] = 1
        pasture[tmp[2]-1][tmp[3]-1][0] = 1
    elif tmp[1]-tmp[3] > 0:
        pasture[tmp[0]-1][tmp[1]-1][3] = 1
        pasture[tmp[2]-1][tmp[3]-1][1] = 1
    else :
        pasture[tmp[0]-1][tmp[1]-1][1] = 1
        pasture[tmp[2]-1][tmp[3]-1][3] = 1

# 목초지에 소가 있는지 없는지
for _ in range(k):
    tmp = list(map(int, sys.stdin.readline().split()))
    cows[tmp[0]-1][tmp[1]-1] = 1

#목초지를 분류했는지 확인
visited = []
# 길없이 다닐수 있는 목초지에 있는 소들의 수를 담을 리스트
num_cows_list = []
for i in range(n):
    for j in range(n):
        # 아직분류 되지 않은 목초지들에 대해서
        if not [i,j] in visited:
            tmp_v, tmp_n = BFS(pasture, cows, [i,j])
            visited.extend(tmp_v)
            num_cows_list.append(tmp_n)
pairs = 0
#목초지 그룹을 2군데 뽑는 방법
rgs = list(combinations(num_cows_list, 2))
for rg in rgs:
    pairs += rg[0]*rg[1]
    
print(pairs)

