# 2000*2000*28 = 112메가, 메모리 초과 주의
# 최소신장트리, 방문한곳을 기록하면 메모리 초과
# 크루스칼 알고리즘 사용, 프림알고리즘 사용하면 메모리 초과

import sys
import heapq

N,C = map(int, sys.stdin.readline().split())
list_field = []
# 모든 노드의 윗 노드는 자기자신을 가리키고 있다. 글로벌 변수
parents = [i for i in range(N)]

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    list_field.append([x,y])

# 모든 노드 사이 비용을 저장할 최소힙    
graph = []
# 모든 노드 사이의 비용을 최소힙으로 담아 저장한다.
for i in range(len(list_field)):
    for j in range(i+1, len(list_field)):
        x1, y1 = list_field[i]
        x2, y2 = list_field[j]
        cost= (x2-x1)**2 + (y2-y1)**2      
        if cost >= C:
            heapq.heappush(graph, [cost,i,j])         

# 유니온과 파인드를 안쓰면 메모리 초과가 남 파이썬이 int 메모리로 28바이트 사용
def find(node):
    # 자신이 최초 노드이면 자신을 반환
    if parents[node] == node:
        return node
    else:
        # 그렇지 않으면 계속해서 위로 올라가서 최초를 반환함
        parents[node] = find(parents[node])
        return parents[node]
    
def union(n1, n2):
    r1, r2 = find(n1), find(n2)
    # 두 노드의 시작이 서로 같다면, 이미 연결된 노드이므로 False 반환
    if r1==r2:
        return False
    # 그렇지 않다면
    else:
        # 한쪽 노드의 루트 노드를 다른 한쪽의 루트 노드로 정한다.(while 문 안쪽과 순서만 맞추면 된다.)
        parents[r2]=r1
        return True
total_cost = 0
edges= 0

while graph:
    
    cost, i, j = heapq.heappop(graph)
    # 노드 i 와 j 가 연결 가능하다면(이미 연결되어있지 않다면)
    if union(i,j) :
        # 연결하고, 노드 j의 부모노드를 i로한다.
        parents[j] == i
        # 비용 합산
        total_cost += cost
        # 그리고 연결된 그래프 수에 1추가
        edges += 1
        # 모두 연결 하였으면 탈출
        if edges == N-1:
            break
#모두 연결 하였으면 비용 출력     
if edges == N-1:
    print(total_cost)
# 그렇지 못했으면 -1 출력
else:
    print(-1)