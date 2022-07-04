# 2000*2000*28 = 112메가, 메모리 초과 주의
# 최소신장트리, 방문한곳을 기록하면 메모리 초과

import sys
import heapq

sys.stdin = open("5th\\input", "r")

N,C = map(int, sys.stdin.readline().split())
list_field = []
parents = [i for i in range(N)]

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    list_field.append([x,y])
    
graph = []
for i in range(len(list_field)):
    for j in range(i+1, len(list_field)):
        x1, y1 = list_field[i]
        x2, y2 = list_field[j]
        cost= (x2-x1)**2 + (y2-y1)**2
        if cost >= C:
            heapq.heappush(graph, [cost,i,j])         


def find(node):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(n1, n2):
    r1, r2 = find(n1), find(n2)
    if r1==r2:
        return False
    else:
        parents[r2]=r1
        return True
total_cost = 0
edges= 0
while graph:
    cost, i, j = heapq.heappop(graph)
    if union(i,j) :
        parents[j] == i
        total_cost += cost
        edges += 1
        if edges == N-1:
            break
if edges == N-1:
    print(total_cost)
else:
    print(-1)