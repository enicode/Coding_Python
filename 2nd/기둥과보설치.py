# 엄청느림, 다른 방법이 있는거 같음
import copy
def solution(n, build_frame):
    answer = [[]]
    size = n # 왜 주는 변수인지 모르겠습니다.
    # 설치된 기둥과 보 가리지 않고 저장할 리스트
    structure=[]
    # 설치된 보만 순서대로 저장할 리스트
    beams = []
    # 설치된 기둥만 순서대로 저장할 리스트
    columns =[]
    
    # 주문대로 건설을 시작한다.
    for order in build_frame:
        # 만약 삭제 주문이라면
        if order[3] == 0:
            # 가능하다면
            if isPossible(order,beams,columns):
                # 현재 건설중인 건물에서 해당 구조물을 철거한다.
                structure.remove(order[:3])
                # 철거물이 기둥이라면
                if order[2] == 0:
                    columns.remove(order[:2])
                #철거물이 보라면
                else:
                    beams.remove(order[:2])
        else:
            # 만약 기둥을 설치하라고 했다면
            if order[2] == 0:
                # 설치 가능한 기둥인지 확인하고
                if isRightColumn(order,beams,columns):
                    # 각각 리스트에 추가
                    structure.append(order[:3])
                    columns.append(order[:2])                                                    
            # 만약 보를 설치하라고 했다면
            else:
                # 설치 가능한 보인지 확인하고
                if isRightBeam(order,beams,columns):
                    # 각각 리스트에 추가
                    structure.append(order[:3])
                    beams.append(order[:2]) 
    # 문제에서 원하는 순서대로 정렬
    structure.sort(key = lambda x :(x[0],x[1],x[2]))
    answer = structure
    return answer

# 가능한 기둥인지?
def isRightColumn(order,beams,columns):
    # 바닥 위에 있거나
    if order[1]==0:
        return True
    # 보의 한쪽 끝 부분 위에 있거나
    if [order[0],order[1]] in beams or [order[0]-1,order[1]] in beams:
        return True    
    # 다른 기둥 위에 있거나
    if [order[0],order[1]-1] in columns:
        return True
    return False

#가능한 보인지?
def isRightBeam(order,beams,columns):   
    # 한쪽 끝이 기둥 위에 있거나
    if [order[0],order[1]-1] in columns or [order[0]+1,order[1]-1] in columns:
        return True
    # 양쪽 끝이 보와 연결되어 있거나            
    if [order[0]-1,order[1]] in beams and [order[0]+1,order[1]] in beams:
        return True
    return False

# 지울수 있는지 없는지
def isPossible(d,beams,columns):
    # 지우고 난 뒤 보들
    blueBeams =copy.deepcopy(beams)
    # 지우고 난 뒤 기둥들
    blueColumns = copy.deepcopy(columns)
    # 기둥을 철거하라고 했다면
    if d[2] == 0:
        # 중복건설이 없으므로 이렇게 삭제가 가능하다.
        blueColumns.remove(d[:2])
        # 건설로 인해 불가능해진 보나 기둥이 없는지 확인한다.
        for beam in blueBeams :
            if isRightBeam(beam, blueBeams, blueColumns):
                pass
            else: 
                return False
        for columns in blueColumns:
            if isRightColumn(columns, blueBeams, blueColumns):
                pass
            else: 
                return False                        
    else:
        # 보를 철거하라고 했다면, 
        blueBeams.remove(d[:2])
        for beam in blueBeams :
            if isRightBeam(beam, blueBeams, blueColumns):
                pass
            else: 
                return False
        for columns in blueColumns:
            if isRightColumn(columns, blueBeams, blueColumns):
                pass
            else: 
                return False    
            
    return True

n = 5
b = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, b))


# b = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# b = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]