def solution(board, skill):
    answer = 0
    r_len = len(board)
    c_len = len(board[0])
    accum_board = [[0 for i in range(c_len)] for j in range(r_len)]
    for sk in skill:
        accum_board[sk[1]][sk[2]] += sk[5] if sk[0] == 1 else -sk[5]
        if sk[4] < c_len-1 and sk[3] < r_len-1:
            accum_board[sk[3]+1][sk[4]+1] += sk[5] if sk[0] == 1 else -sk[5]
        if sk[4] < c_len-1:
            accum_board[sk[1]][sk[4]+1] -= sk[5] if sk[0] == 1 else -sk[5]
        if sk[3] < r_len-1:
            accum_board[sk[3]+1][sk[2]] -= sk[5] if sk[0] == 1 else -sk[5]
    
    damage = [[0 for i in range(c_len)] for j in range(r_len)]
    
        
    for i in range(r_len):
        row_sum = 0
        for j in range(c_len):
            if i==0 and j == 0:
                damage[0][0] = accum_board[0][0]
            elif i ==0:
                damage[0][j] = sum(accum_board[0][:j+1])
            else:
                row_sum += accum_board[i][j]
                damage[i][j] = damage[i-1][j]+row_sum
                
            if board[i][j] - damage[i][j] > 0:
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