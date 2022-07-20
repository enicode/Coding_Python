# 최소 신장 트리, 크루스칼 알고리즘
import sys
import heapq

sys.stdin = open('7th\\iuput', 'r')
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# 부모 노드 정보, 시작할 때는 모두 자기 자신을 가리키고 있다.
parents = [i for i in range(N+1)]
# 간선 정보(최소힙에 담는다, 중요한건 최소비용이므로)
edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, [c,a,b])
# 초기에 연결을 시작할 컴퓨터 1
connected = 1
tot_cost = 0
# 유니온과 파인드는 진짜 노드가 이어진 것을 구현해주는 것이 아닌, 서로 연결되었는지 아닌지만 알려주는 함수
# 서로 분리된 두 노드를 합칠 수 는지 보는 함수
# 자신의 루트노드를 찾는 함수
def find(n):
    if parents[n] == n:
        return n
    else:
        parents[n] = find(parents[n])
        return parents[n]
def union(n1,n2):
    # 들어온 노드들의 최초 노드들을 찾는다.
    r1, r2 = find(n1), find(n2)
    # 같다면 이미 연결된 노드이므로 False 반환
    if r1 == r2:
        return False
    # 아니라면
    else:
        # 한쪽 최초 노드의 부모노드를 다른 한쪽의 최초 노드로 바꾼다. 이렇게 함으로서 양쪽의 최초노드가 같아지고 실제 연결 구조에 관계없이 연결되었음을 알려줄수 있다. 
        # 단, while 문과 안쪽 유니온 다음과 순서를 맞춰야한다. 
        parents[r2] = r1
        return True
while edges:
    cost, i, j = heapq.heappop(edges)
    # 두 노드가 서로 이미 연결된 노드가 아니라면, 어느 한쪽의 부모노드를 다른 한쪽 노드로 바꾼다. 그리고 비용을 추가한다.
    if i != j:
        if union(i, j):
            parents[j] = i
            tot_cost += cost
            #연결된 컴퓨터 수를 증가 시킨다.
            connected += 1
            #컴퓨터를 모두 연결하였으면 while 문을 종료한다.
            if connected == N:
                break
    
print(tot_cost)
