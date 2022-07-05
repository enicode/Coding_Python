# BFS
# 그 동영상과 USADO가 k 이상이 모든 동영상의 숫자
# 동영상 노드를 넘어가다가 USADO가 k 미만이 될때까지 찾는다.
# 그때까지 동영상 숫자를 반환한다.
# 딕셔너리를 만든다. 딕셔너리에는 동영상 q에 대한 모든 연결된 다른 동영상들의 정보와 유사도를 쌍을 지어 담는다.
# 이제 딕셔너리를 방문하는데, BFS 로 탐색한다.
import sys
from collections import deque

def solution(dic, k, v):
    visited = [0 for i in range(N)]
    queue = deque([v])
    answer = 0
    while queue:
        n = queue.popleft()
        visited[n] = 1
        try:
            #동영상 n과 관계있는 모든 동영상들에 대하여
            for val in dic[n]:
                # USADO가 k 이상이고 방문한적이 없는 동영상 노드라면, 큐에 추가하고 추천될 동영상 갯수에 1을 더한다.
                if val[1] >= k and not visited[val[0]]:
                    answer +=1
                    queue.append(val[0])
                    visited[val[0]] = 1
        except:
            pass
    return answer

N,Q = map(int, sys.stdin.readline().split())

# USADO를 담을 딕셔너리를 만든다.
usa_dict = {}
# p번째 동영상과 q번째 동영상 사이의 유사도 r을 담는다.
for _ in range(N-1):
    p,q,r = map(int, sys.stdin.readline().split())
    try:   
        usa_dict[p-1].append([q-1,r])
    except KeyError:
        usa_dict[p-1] = [[q-1,r]]
    try:
        usa_dict[q-1].append([p-1,r])
    except KeyError:
        usa_dict[q-1] = [[p-1,r]]
            
for i in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(solution(usa_dict, k, v-1))
    
    

    