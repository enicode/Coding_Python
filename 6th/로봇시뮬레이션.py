import sys

sys.stdin = open("6th\\input",'r')

A, B = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

board = [[0 for i in range(B)] for j in range(A)]
# 로봇 번호 1 부터 시작하게 0 에는 자리채우기용 None
robots= [None]
# 시계, 반시계 회전을 편하게 해줄 튜플
nesw= ('N','E','S','W')

# 로봇의 움직임을 구현할 함수
def move(n, d):
    # 왼쪽으로 회전 (N->E->S->W)의 역순
    if d == "L":
        robots[n][2] = (robots[n][2]-1)%4
        return True
    # 오른쪽으로 회전 (N->E->S->W)의 순
    if d == "R":
        robots[n][2] = (robots[n][2]+1)%4
        return True
    # 로봇이 움직이므로 보드에서 그 로봇의 위치를 먼저 삭제한다.(다음으로 옮기기 전에)
    # 그런데 그 방향으로 진행하면 벽을 만나거나 다른 로봇이 있는 공간으로 간다면 적절한 문구를 출력하고 프로그램을 종료한다.
    # 갈 수 있는 공간이면 그 로봇의 좌표를 움직이고, 보드에도 그 로봇이 있다고 기록한다.
    if d == "F":
        board[robots[n][0]][robots[n][1]] = 0
        if robots[n][2] == 0:
            if robots[n][1] >= B-1:
                print(f'Robot {n} crashes into the wall')
                sys.exit()
            next = board[robots[n][0]][robots[n][1]+1]
            if next:
                print(f'Robot {n} crashes into robot {next}')
                sys.exit()
            robots[n][1] += 1
            board[robots[n][0]][robots[n][1]] = n
        if robots[n][2] == 1:
            if robots[n][0] >= A-1:
                print(f'Robot {n} crashes into the wall')
                sys.exit()
            next = board[robots[n][0]+1][robots[n][1]]
            if next:
                print(f'Robot {n} crashes into robot {next}')
                sys.exit()
            robots[n][0] += 1
            board[robots[n][0]][robots[n][1]] = n
        if robots[n][2] == 3:
            if robots[n][0] <= 0:
                print(f'Robot {n} crashes into the wall')
                sys.exit()
            next = board[robots[n][0]-1][robots[n][1]]
            if next:
                print(f'Robot {n} crashes into robot {next}')
                sys.exit()
            robots[n][0] -= 1
            board[robots[n][0]][robots[n][1]] = n 
        if robots[n][2] == 2:
            if robots[n][1] <= 0:
                print(f'Robot {n} crashes into the wall')
                sys.exit()
            next = board[robots[n][0]][robots[n][1]-1]
            if next:
                print(f'Robot {n} crashes into robot {next}')
                sys.exit()
            robots[n][1] -= 1
            board[robots[n][0]][robots[n][1]] = n

# 로봇의 정보를 받는다.
for i in range(N):
    # 로봇의 x,y, 방향
    x, y, d = sys.stdin.readline().strip().split()
    x = int(x) - 1 
    y = int(y) - 1
    if d == 'N':
        d = 0
    if d == 'E':
        d = 1
    if d == 'S':
        d = 2
    if d == 'W':
        d = 3
    # 로봇의 번호를 보드에 기록한다.
    board[x][y] = i+1
    # 로봇을 순서대로 리스트에 기록한다.
    robots.append([x,y,d])
# 명령(M개)를 받아 수행한다.
for _ in range(M): 
    robot_n, o, times = sys.stdin.readline().strip().split()
    robot_n = int(robot_n)
    times = int(times)
    for _ in range(times):
        move(robot_n, o)
else:
    print("OK")