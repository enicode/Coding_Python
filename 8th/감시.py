# 15683번 - 감시 
# 감시카메라 방향은 최대 4방향, 카메라의 갯수는 8개, 4^8 =65536 완전탐색
# 
import sys
import copy
sys.stdin = open('8th\input','r')
N, M = map(int, sys.stdin.readline().split())

office = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cameras= []
for i in range(len(office)):
    for j in range(len(office[i])):
        ct = [1,2,3,4,5]
        if office[i][j] in ct:
            cameras.append([[i,j],office[i][j]])
# 감시카메라가 보는 영역을 # 처리 해서 사무실을 상태를 돌려주는 함수
# 인자로 사무실 상태, 카메라위치, 카메라종류, 카메라가 보는 방향을 받는다.
def monitor(o, cp, ct, d):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    office = o
    if ct == 1:
        y,x = cp
        while True:
            # 한방향 감시카메라이므로, 한방향만 검색하면 된다. 
            x += dx[d]
            y += dy[d]
            # 경계
            if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                break
            # 6을 만나면 벽이므로 while문을 탈출한다.
            if office[y][x] == 6:
                break
            # 다른 감시카메라를 만나면, pass 한다.
            if office[y][x] in [1,2,3,4,5]:
                pass
            # 다른 경우(0) , #으로 바꾼다.
            else:
                office[y][x] = '#'
    elif ct == 2:
        # 2번 카메라는 양방향이므로
        ds = [d, (d+2)%4]
        for i in ds:
            y,x = cp
            while True: 
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                    break
                if office[y][x] == 6:
                    break
                if office[y][x] in [1,2,3,4,5]:
                    pass
                else:
                    office[y][x] = '#'
    elif ct == 3:
        # 3번 카메라는 90도 방향이므로
        ds = [d, (d+3)%4]
        for i in ds:
            y,x = cp
            while True: 
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                    break
                if office[y][x] == 6:
                    break
                if office[y][x] in [1,2,3,4,5]:
                    pass
                else:
                    office[y][x] = '#'        
    elif ct == 4:
        # 4번 카메라는 ㅗ 방향이므로
        ds = [d, (d+2)%4,(d+3)%4]
        for i in ds:
            y,x = cp
            while True: 
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                    break
                if office[y][x] == 6:
                    break
                if office[y][x] in [1,2,3,4,5]:
                    pass
                else:
                    office[y][x] = '#'
    else:
        # 5번 방향은 모든 방향이므로
        ds = [d,(d+1)%4,(d+2)%4,(d+3)%4]
        for i in ds:
            y,x = cp
            while True: 
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                    break
                if office[y][x] == 6:
                    break
                if office[y][x] in [1,2,3,4,5]:
                    pass
                else:
                    office[y][x] = '#'
    return office
# 사무실 상태, 카메라 리스트를 넣으면 답을 반환하는 재귀함수
def solution(o, cs):
    # 초기 비교용 값, 모든 사무실이 사각지대라고 가정
    answer =N*M
    office = o   
    directions = [0,1,2,3]
    # 이제 확인할 카메라가 남지 않았으면, 그 때 사각지대의 수를 세서 반환한다.
    if not cs:
        answer = 0
        for line in office:
            answer += line.count(0)
        return answer
    # 카메라를 방향마다 돌려가며 확인한다.
    for d in directions:
        # 방향 돌리기 전 상태를 깊은 복사로 복사해둔다.
        original = copy.deepcopy(office)
        # 카메라 감시 범위를 표시 한다.
        office = monitor(office, cs[0][0], cs[0][1], d)
        # 그 카메라는 감시 범위를 표시했으므로, 카메라리스트에서 뺴고 다음 카메라부터를 카메라 리스트로 한다.
        others = cs[1:]
        # 사각지대를 최소화하는 값을 선택한다.
        answer = min(answer, solution(office, others))
        # 사무실 상태를 원래대로 돌려놓는다.
        office = original
    return answer
        
print(solution(office,cameras))