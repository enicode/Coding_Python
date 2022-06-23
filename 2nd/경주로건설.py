def solution(board):
    answer = -1
    # 좌표, [왔던 방향, 나갔던 방향] 여태까지 비용
    q = [[0,0,-1,0]]
    size = len(board)
    costBoard = [[-1 for _ in range(size)] for _ in range(size)]
    # costBoard[비용,[지금까지 왔던 방향,지금까지 갔던 방향]]
    costBoard[0][0] = 0
    # 루트가 남아 있는 동안 반복한다
    while q:
        # 루트의 마지막에서 다시 시작한다.
        y, x, d ,c = q.pop()
        if [y, x] == [size-1, size-1] and (answer == -1 or answer > c):
            answer = c
        # 갈 수 있는 잠재 방향
        news = [[y+1,x],[y,x+1],[y-1,x],[y,x-1],]       
        # 갈수 있는 모든 방향에 대해서
        for direction, [ny, nx] in enumerate(news):
            # 경계 제외
            if ny <= -1 or ny>= size or nx <=-1 or nx >=size:
                pass
            # 벽 제외
            elif board[ny][nx]:
                pass
            else:         
                cost = 0
                # 처음에 모두 직선, 꺽이면 600 추가 직선이면 100 추가
                if d == direction  or d == -1:
                    cost = c + 100
                else:
                    cost = c + 600
                # 만약 처음 계산하는 거면
                if costBoard[ny][nx] == -1:
                    q.append([ny, nx, direction, cost])
                    costBoard[ny][nx] = cost
                else:
                    # 만약 계산한 값이 있더라도 그 차이가 코너 건설비용 차이 안쪽으로 난다면 그 경로 이후에 다시 코너가 생길지 아닐지 차이로 그 차이를 메울수도 있으므로 버려서는 안됨
                    if cost <= costBoard[ny][nx] + 400:
                        q.append([ny, nx, direction, cost])
                        costBoard[ny][nx] = cost                                                          
    return answer
       
board =[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]

print(solution(board))
