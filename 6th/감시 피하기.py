import sys

sys.stdin = open("6th\\input", "r")
N = int(sys.stdin.readline())
# 학생의 위치와 선생님 위치를 저장할 2차원 배열
board = [["X" for i in range(N)] for j in range(N)]
# 학생의 위치정보를 저장할 리스트,
students = []
# 위치정보 저장
for i in range(N):
    tmp = list(sys.stdin.readline().split())
    for j in range(N):
        if tmp[j] == "S":
            students.append([i,j])
        board[i][j] = tmp[j]
# 설치된 장애물의 숫자
installed = 0
# 피할 수 있는지 없는지 알려주는 함수,       
def avoid(c):
    for stu in students:
        # 학생을 기준으로 좌우상하로 나아가다가 O 만나면 더 이상 검색할 필요 없으므로 for문 종료, T를 만나면 False 반환
        for i in range(1,stu[0]+1):
            if c[stu[0]-i][stu[1]] == "O":
                break
            if c[stu[0]-i][stu[1]] == "T":
                return False
        for i in range(stu[0]+1,N):
            if c[i][stu[1]] == "O":
                break
            if c[i][stu[1]] == "T":
                return False
        for i in range(1,stu[1]+1):
            if c[stu[0]][stu[1]-i] == "O":
                break
            if c[stu[0]][stu[1]-i] == "T":
                return False
        for i in range(stu[1]+1,N):
            if c[stu[0]][i] == "O":
                break
            if c[stu[0]][i] == "T":
                return False
    return True
# 복도 정보, 장애물 설치를 시작할 좌표, 설치된 장애물 숫자가 들어오면 회피 가능한지 알려주는 함수
def solution(b,c,install):
    corridor = b
    ins= install
    x = c[1]
    y = c[0]
    for i in range(y,N):
        # 열의 시작은 처음에만 들어온 값에 영향을 받고 다음부터는 0부터(처음부터) 시작한다. (x,y) 부터 설치 시작!
        start = x if i == y else 0
        for j in range(start,N):
            # 현 위치에 아무것도 없다면 장애물을 하나 설치한다. 설치하지 못하면 다음 위치로 간다.
            if corridor[i][j] != "S" and corridor[i][j] != "T":    
                corridor[i][j] = "O"
                # 설치하였으므로 설치 갯수 +1
                ins += 1
                # 만약 그렇게 했는데 장애물이 3개라면
                if ins >= 3:
                    # 그 때 피할수 잇다면 true 반환
                    if avoid(corridor): return True
                    # 만약 피할 수 없다면 마지막 장애물을 치우고 다음으로 진행한다.
                    else:
                        corridor[i][j] = "X"
                        ins -= 1
                        continue
                # 장애물이 3개가 아니라면 다음 장애물을 설치하러 가는데, 지금 위치 다음 위치부터 시작하여 선택한다.
                else:
                    # 만약 이번이 마지막 위치라면 더이상 설치할 수 없으므로, False를 반환한다.
                    if i == N-1 and j == N-1: return False
                    # 아니라면 위치에 따라서 다음 위치부터 장애물을 설치한다.
                    # 마지막 열부터 시작한다면, 다음 행부터
                    elif j == N-1: 
                        if solution(corridor, [i+1,0], ins):
                            return True
                    # 마지막 열이 아니라면 다음 열부터
                    else: 
                        if solution(corridor, [i,j+1], ins):
                            return True
                # 이번에 설치한 장애물에 대해서 검사가 다 끝났으므로 장애물을 제거하고, 다음 위치로 이동한다.
                corridor[i][j] = "X"
                ins -= 1
  
if solution(board,[0,0],installed):
    print("YES")
else:
    print("NO")