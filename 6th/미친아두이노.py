import sys
# 리스트를 쓰고 지울일이 많으면 deque를 쓰는 것이 좋다.
from collections import deque
sys.stdin = open("6th\\input","r")

R, C = map(int,sys.stdin.readline().split())
# 보드
board =[["." for i in range(C)] for j in range(R)]
# 미친 아두이노들 겹치는 거 볼 보드
adu_board =[[[deque(),0] for i in range(C)] for j in range(R)]
# 미친 아두이노들의 위치
mad = deque()
# 종수의 위치
js = []
for i in range(R):
    tmp = sys.stdin.readline()
    for j in range(C):
        if tmp[j] == 'R':
            mad.append([i,j])
        if tmp[j] == 'I':
            js = [i,j]
# 종수의 움직임을 담을 deque
moves = deque()
# 그냥 담으면 typeerror, 입력에 \n 같은것이 있는듯?
tmp = sys.stdin.readline().split()
for str in tmp:
    for move in str:
        moves.append(int(move))
# 종수를 움직이는 함수
def jsmove(a,c):
    if a == 1:
        return [c[0]+1,c[1]-1]
    if a == 2:
        return [c[0]+1,c[1]]
    if a == 3:
        return [c[0]+1,c[1]+1]
    if a == 4:
        return [c[0],c[1]-1]
    if a == 5:
        return [c[0],c[1]]
    if a == 6:
        return [c[0],c[1]+1]
    if a == 7:
        return [c[0]-1,c[1]-1]
    if a == 8:
        return [c[0]-1,c[1]]
    if a == 9:
        return [c[0]-1,c[1]+1]
# 미친 아두이노들을 움직일 함수        
def madmove(jongsu,madadu):
    dy = int((jongsu[0]-madadu[0])/abs(jongsu[0]-madadu[0])) if jongsu[0] != madadu[0] else 0
    dx = int((jongsu[1]-madadu[1])/abs(jongsu[1]-madadu[1])) if jongsu[1] != madadu[1] else 0
    return [madadu[0]+dy,madadu[1]+dx]
# 턴과, 끝남을 알려줄 지표 
turn = 0
end_check = False
while moves:
    turn += 1
    # 종수를 움직인다.
    js = jsmove(moves.popleft(),js)
    # 미친 아두이노를 움직인다.
    for i in range(len(mad)):
        # 그 번호의 미친 아두이노가 살아 있을 때
        if mad[i] != None:
            mad[i] = madmove(js,mad[i])
            # 움직인 결과 종수와 만나면 게임이 끝난다.
            if mad[i] == js :
                end_check = True
                print(f'kraj {turn}')
                break
    # 게임이 끝나면 while 문을 빠져나온다
    if end_check:break
    # adu_board에 미친 아두이노들을 겹쳐서 센다 adu_board[r[0]][r[1]][1] 는 겹쳐진 횟수, adu_board[r[0]][r[1]][0] 는 겹처진 아두이노들 번호 리스트
    for i, r in enumerate(mad):
        if r != None:
            adu_board[r[0]][r[1]][1] += 1
            adu_board[r[0]][r[1]][0].append(i)
            # 만약 이중 이상으로겹치면
            if adu_board[r[0]][r[1]][1] >= 2:
                # 그 위치에 있는 미친 아두이노들을 죽인다.
                while adu_board[r[0]][r[1]][0]:
                    mad[adu_board[r[0]][r[1]][0].pop()] = None
    # adu_board 초기화
    adu_board =[[[deque(),0] for i in range(C)] for j in range(R)]
# 종료후 아두이노와 미친 아두이노들의 위치를 기록할 보드            
board =[["." for i in range(C)] for j in range(R)]
# 아두이노 위치 기록
board[js[0]][js[1]] = 'I'
# 종료 후 남아있는 아두이노들만 기록
for m in mad:
    if m != None:
        board[m[0]][m[1]] = 'R'

if not end_check:
    for line in board:
        for p in line:
            print(p, end="")
        print()