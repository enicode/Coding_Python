# 2차원배열 => 메모리 초과
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
    a,b,m = map(int,sys.stdin.readline().split())
    heapq.heappush(edges, [-m, a, b])

f1, f2 = map(int, sys.stdin.readline().split())
        
def find(n):
    if parents[n] == n:
        return n
    else:
        parents[n] = find(parents[n])
        return parents[n]
bit_f1 = 1<<f1
bit_f2 = 1<<f2
global answer
answer = 0
while edges:
    m, a, b = heapq.heappop(edges)
    try:
        # a에 연결된 노드들 중에
        for i in range(len(nodes[a])):
            if nodes[a][i][0] == b and nodes[a][i][1] < m:
                nodes[a][i] = [b,-m]
            else:
                nodes[a].append([b,-m])
    except KeyError:
        nodes[a] = [[b,-m]]
    try:
        # b에 연결된 노드들 중에
        for i in range(len(nodes[b])):
            if nodes[b][i][0] == b and nodes[b][i][1] < m:
                nodes[b][i] = [a,-m]
            else:
                nodes[b].append([a,-m])
    except KeyError:
        nodes[b] = [[a,-m]]
    
    r1, r2 = find(a), find(b)
    if r1 != r2:
        parents[r1] = r2
        parents[a] = b
    p1, p2 = find(f1), find(f2)
    if p1 == p2:
        answer = -m
        break
print(answer)