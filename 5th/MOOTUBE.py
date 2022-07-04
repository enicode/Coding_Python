# 그 동영상과 USADO가 k 이상이 모든 동영상의 숫자
# 동영상 노드를 넘어가다가 USADO가 k 미만이 될때까지 찾는다.
# 그때까지 동영상 숫자를 반환한다.
# 2차원 배열을 만든다. (행,열) 의 값이 행에서 열로 사이 USADO라 하자. 이 행렬은 대칭 행렬
import sys
from collections import deque

sys.stdin = open("5th\\input", "r")

def solution(dic, k, v):
    visited = [0 for i in range(N)]
    queue = deque([v])
    answer = 0
    while queue:
        n = queue.popleft()
        visited[n] = 1
        try:
            for val in dic[n]:
                if val[1] >= k and not visited[val[0]]:
                    answer +=1
                    queue.append(val[0])
                    visited[val[0]] = 1
        except:
            pass
    return answer

N,Q = map(int, sys.stdin.readline().split())

usa_dict = {}

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
    
    

    