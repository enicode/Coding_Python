# 시간이 부족하다, 정렬이나, 누적합 등을 제외하고는 사용할 수 없을 것 같다.
# 배열이므로 누적합을 그냥 쓸수 는 없다. 2차원에 맞게 끔 변형
# 어느 지점에 영향을 미칠 수 있는 스킬은 기준점(r0,c0) 원점으로 하여 좌표평면을 만들면
# x,y축을 포함한 4사분에서 시작하는 스킬뿐이다. 따라서 어떤 점을 기준으로 하여 거기까지 스킬 누적합을 구하면 된다.
# 그런데 그 스킬의 범위가 끝났는지도 알아야한다. 보통 누적합을 쓸 데 처럼 행방향 끝+1과 열방향 끝+1에 -값을 추가해보면
# 행방향과 열방향 모두 바깥인 경우는 0 이 아닌 - 값이 된다. 맞게 해주려면, (행방향 끝+1, 열방향 끝+1)에 다시 + 값을 추가하면 된다.
def solution(board, skill):
    answer = 0
    # 행길이(세로)
    r_len = len(board)
    # 열길이(가로)
    c_len = len(board[0])
    #누적합을 만들 정보를 저장할 배열
    accum_board = [[0 for i in range(c_len)] for j in range(r_len)]
    for sk in skill:
        # r1,c1에 데미지나 회복을 더해준다.
        accum_board[sk[1]][sk[2]] += sk[5] if sk[0] == 1 else -sk[5]
        # r2,c2에 데미지나 회복을 더해준다.(범위가 끝까지인 스킬은 기록 X)
        if sk[4] < c_len-1 and sk[3] < r_len-1:
            accum_board[sk[3]+1][sk[4]+1] += sk[5] if sk[0] == 1 else -sk[5]
        # r1, c2에 데미지나 회복의 - 값을 더해준다.
        if sk[4] < c_len-1:
            accum_board[sk[1]][sk[4]+1] -= sk[5] if sk[0] == 1 else -sk[5]
        # r2, c1에 데미지나 회복의 - 값을 더해준다.
        if sk[3] < r_len-1:
            accum_board[sk[3]+1][sk[2]] -= sk[5] if sk[0] == 1 else -sk[5]
    # 총 데미지를 기록할 배열
    damage = [[0 for i in range(c_len)] for j in range(r_len)]
    
    # 데미지를 한 행씩 채워나간다.     
    for i in range(r_len):
        # 행방향 누적합(가로)
        row_sum = 0
        for j in range(c_len):
            # 초깃값은 (0,0)에서 시작하는 데미지와 회복의 합
            if i==0 and j == 0:
                damage[0][0] = accum_board[0][0]
            # 초깃값을 제외하고 첫행은 일반적인 누적합처럼 구하면 된다.
            elif i ==0:
                damage[0][j] = sum(accum_board[0][:j+1])
            # 두번째 행부터는 같은 열 바로 윗행 까지 누적합 + 행방향 누적합이 그 지점의 값이된다.
            else:
                row_sum += accum_board[i][j]
                damage[i][j] = damage[i-1][j]+row_sum
            # 체력이 데미지를 초과하면 +1     
            if board[i][j] > damage[i][j]:
                answer += 1
    
    return answer 
            
            
            

board = [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]]

skill =[[1,0,0,2,2,1]]

print(solution(board, skill))


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))
board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))

'''
            print(dmg)
            
            if j < c_start_idx[0]:
                dmg  +=0 
            elif j > c_start_idx[-1]:
                dmg += c_start_dmg[-1]
            else:    
                tmp = bisect_left(c_start_idx, j)
                c_start = tmp
                dmg += c_start_dmg[c_start] 
            print(dmg)
            
            if i < r_end_idx[0]:
                dmg  +=0 
            elif i > r_end_idx[-1]:
                dmg += r_end_dmg[-1]
            else:    
                tmp = bisect_left(r_end_idx, i)
                r_end = tmp
                dmg += r_end_dmg[r_end]           
            print(dmg)
            
            if j < c_end_idx[0]:
                dmg  +=0 
            elif j > c_end_idx[-1]:
                dmg += c_end_dmg[-1]
            else:    
                tmp = bisect_left(c_end_idx, j)
                c_end = tmp
                dmg += c_end_dmg[c_end]
            print(dmg)
'''