# 다익스트라 알고리즘 문제
# 시작 지점과 특정 지점 까지 최소 비용을 구한다.
# 특정 지점부터 각자의 도착점 까지 최소 비용을 구한다
# 두 비용을 합치고, 가장 적은 것을 택한다. 
def solution(n, s, a, b, fares):
    answer = 0
    # 지점과 지점사이가 연결되어있는지와 되어있다면 그 요금을 저장하는 2차원배열
    matrix = [[[0,1] for i in range(n)] for j in range(n)]
    
    for fare in fares:
        matrix[fare[0]-1][fare[1]-1] = [fare[2],1]
    # 대칭적으로 만들어 준다
    for i in range(n):
        for j in range(i):
            if matrix[i][j][0]:
                matrix[j][i] = matrix[i][j]
            elif matrix[j][i][0]:
                matrix[i][j] = matrix[j][i]
    # 시작지점에서 모든 지점 까지 최소비용    
    sMinD = modifiedDijk(s-1,matrix)
    # A 지점에서 모든 지점 까지 최소비용
    aMinD = modifiedDijk(a-1,matrix)
    # B 지점에서 모든 지점까지 최소비용
    bMinD = modifiedDijk(b-1,matrix)
    
    minimum = 300000000
    # 모든 헤어지는 노드에 대해서 최소값을 찾는다.
    for node in range(n):
        tmp = sMinD[node][1]+aMinD[node][1]+bMinD[node][1]
        if  tmp <minimum:
            minimum = tmp
    answer = minimum
    return answer    
    
    
    
# 다익스트라 알고리즘    
def modifiedDijk(start, matrix):
    minD = [ [i,100000000] for i in range(len(matrix))]
    nodes= [i for i in range(len(matrix))]
    prev = []
    startNode = start
    minD[startNode][1] = 0
    nodes.remove(startNode)
    prev.append(startNode)
    for (i,neighbor) in enumerate(matrix[startNode]):
            if neighbor[0]:
                minD[i][1] = neighbor[0]
    while nodes:
        min = 100000000
        tmp = startNode
        for i,md in enumerate(minD):
            if i in nodes:
                if md[1] < min:
                    min = md[1]
                    startNode = i
        if startNode == tmp:
            startNode = nodes[0]
        prev.append(startNode)
        nodes.remove(startNode)
        for (i,neighbor) in enumerate(matrix[startNode]):
            if neighbor[0]:
                d = neighbor[0] + minD[startNode][1]
                if  d < minD[i][1]:
                    minD[i][1] = d
                    
    return minD
                    
                
                
        
    




n, s, a, b =6, 4, 6, 2
fares =[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s,a,b,fares))

n, s, a, b = 7, 3, 4, 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n,s,a,b,fares))

n, s, a, b = 6, 4, 5, 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n,s,a,b,fares))