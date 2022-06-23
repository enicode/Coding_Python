# 엄청느림, 다른 방법이 있는거 같음
import copy
def solution(n, build_frame):
    # 그 좌표에 건설된 [기둥, 보] 리스트 설치 되었으면 1아니면 0
    matrix = [[[0,0] for _ in range(n+1) ] for _ in range(n+1)]
    answer = []
    # 주문대로 건설을 시작한다.
    for order in build_frame:
        # 만약 삭제 주문이라면
        if order[3] == 0:
            # 가능하다면
            if isPossible(order,matrix):
                # 현재 건설중인 건물에서 해당 구조물을 철거한다.               
                # 철거물이 기둥이라면
                if order[2] == 0:
                    matrix[order[0]][order[1]][0] = 0
                #철거물이 보라면
                else:
                    matrix[order[0]][order[1]][1] = 0
        else:
            # 만약 기둥을 설치하라고 했다면
            if order[2] == 0:
                # 설치 가능한 기둥인지 확인하고
                if isRightColumn(order[:2],matrix):
                    matrix[order[0]][order[1]][0] = 1                                                   
            # 만약 보를 설치하라고 했다면
            else:
                # 설치 가능한 보인지 확인하고
                if isRightBeam(order[:2],matrix):
                    # 각각 리스트에 추가
                    matrix[order[0]][order[1]][1] = 1 
    # 문제에서 원하는 순서대로 정렬
    for i in range(n+1):
        for j in range(n+1):
            if matrix[i][j][0]:
                answer.append([i,j,0])
            if matrix[i][j][1]:
                answer.append([i,j,1])            
    return answer

# 가능한 기둥인지?
def isRightColumn(order,matrix):
    # 바닥 위에 있거나
    if order[1]==0:
        return True
    # 보의 한쪽 끝 부분 위에 있거나
    if 0 < order[0] and order[0]<len(matrix)-1:
        if matrix[order[0]][order[1]][1] or matrix[order[0]-1][order[1]][1]:
            return True
    if order[0] == len(matrix)-1:
        if matrix[order[0]-1][order[1]][1]:
            return True       
    if order[0] == 0:
        if matrix[order[0]][order[1]][1]:
            return True
    # 다른 기둥 위에 있거나  
    if matrix[order[0]][order[1]-1][0]:
        return True
    return False

#가능한 보인지?
def isRightBeam(order,matrix):  
    # 한쪽 끝이 기둥 위에 있거나
    if matrix[order[0]][order[1]-1][0] or matrix[order[0]+1][order[1]-1][0]:
        return True
    # 양쪽 끝이 보와 연결되어 있거나
    # 맨끝에 설치한다면 기둥이 없는 시점에서 탈락 
    if order[0] == len(matrix)-1:
        return False       
    if matrix[order[0]-1][order[1]][1] and matrix[order[0]+1][order[1]][1]:
        return True
    return False

# 지울수 있는지 없는지
def isPossible(d,matrix):
    blue = copy.deepcopy(matrix)
    # 일단 삭제해본다.
    blue[d[0]][d[1]] = [0,0]
    # 건설로 인해 불가능해진 보나 기둥이 없는지 확인한다.
    check = True
    # 기둥이면 위쪽 체크
    if d[2] == 0:
        # 삭제한 기둥 위에 기둥이 있다면
        if matrix[d[0]][d[1]+1][0]:
            check = isRightColumn([d[0],d[1]+1],blue)
            if not check:
                return False
        # 삭제한 기둥 위에 보가 있다면
        if matrix[d[0]][d[1]+1][1]:
            check = isRightBeam([d[0],d[1]+1],blue)
            if not check:
                return False
        # 삭제한 기둥에 보 오른쪽이 지탱되고 있던 보가 있다면
        if matrix[d[0]-1][d[1]+1][1]:
            check = isRightBeam([d[0]-1,d[1]+1],blue)
            if not check:
                return False
    # 보면 양 옆 체크    
    else:
        # 오른쪽에 기둥이 있다면
        if matrix[d[0]+1][d[1]][0]:
            check = isRightColumn([d[0]+1,d[1]],blue)
            if not check:
                return False
        # 그 위치에 기둥이 있다면
        if matrix[d[0]][d[1]][0]:
            check = isRightColumn([d[0],d[1]],blue)
            if not check:
                return False      
        # 오른쪽에 보가 있다면   
        if matrix[d[0]+1][d[1]][1]:
            check = isRightBeam([d[0]+1,d[1]],blue)
            if not check:
                return False
        # 왼쪽에 보가 있다면
        if matrix[d[0]-1][d[1]][1]:
            check = isRightBeam([d[0]-1,d[1]],blue)
            if not check:
                return False                    
            
    return check

n = 5
b = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, b))