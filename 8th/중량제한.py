# 크루스칼 알고리즘
# 간선의 값이 가장 큰 것부터 순서대로 이어 붙이다가, 공장과 공장이 같은 노드로 연결된 순간 이어붙인 간선의 값이 답이다.
# 노드 정보 담는 방법-> 2차원 배열 메모리초과 // 딕셔너리를 사용해서 메모리와, 검색 시간을 모두 줄인다. 같은 부지 사이에 다리가 여러개 있을수 있음을 주의
# 받은 정보는 크루스칼 알고리즘을 사용할 것이므로, 최대힙에 넣고, 하나씩 꺼내쓴다.
import sys
import heapq
sys.stdin = open('8th\\input', 'r')
N,M = map(int,sys.stdin.readline().split())
INF = float('inf')
edges = []
nodes = {}
# 그 노드의 부모노드
parents = [i for i in range(N+1)]
for _ in range(M):
    # 무게제한을 기준으로 최대힙    
    a,b,m = map(int,sys.stdin.readline().split())
    heapq.heappush(edges, [-m, a, b])

f1, f2 = map(int, sys.stdin.readline().split())
# 유니온-파인드에서 파인드 함수        
def find(n):
    if parents[n] == n:
        return n
    else:
        parents[n] = find(parents[n])
        return parents[n]
# 비트 마스크
bit_f1 = 1<<f1
bit_f2 = 1<<f2
answer = 0
while edges:
    # 큰값부터 꺼낸다.
    m, a, b = heapq.heappop(edges)
    try:
        # a에 연결된 노드들 중에 b가 존재하면, 최대제한 무게를 비교하여 크다면 바꾸고, 아니면 그대로 둔다.
        for i in range(len(nodes[a])):
            if nodes[a][i][0] == b and nodes[a][i][1] < m:
                nodes[a][i] = [b,-m]
            # b가 존재 하지 않으면 추가한다.
            else:
                nodes[a].append([b,-m])
    except KeyError:
        nodes[a] = [[b,-m]]
    try:
        # a와b 양쪽으로 연결되었으므로
        for i in range(len(nodes[b])):
            if nodes[b][i][0] == b and nodes[b][i][1] < m:
                nodes[b][i] = [a,-m]
            else:
                nodes[b].append([a,-m])
    except KeyError:
        nodes[b] = [[a,-m]]
    # 들어온 a와 b가 연결된 노드 인지 확인하고, 아닐하면 연결해준다.
    r1, r2 = find(a), find(b)
    if r1 != r2:
        parents[r1] = r2
        parents[a] = b
    # 연결한 뒤에 공장이 연결되었느지 확인한다. 연결되었으면 whlie문을 종료하며 답을 가지고 나온다
    p1, p2 = find(f1), find(f2)
    if p1 == p2:
        answer = -m
        break
print(answer)