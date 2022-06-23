# (6!)*2^6~5만 이므로 완전 탐색으로 풀수 있다.
from itertools import product
from itertools import permutations
import copy
def Number(n1, n2, line):
    number = 0
    check = 0
    n=n1
    step = (n2-n1)//abs(n2-n1)
    n += step
    while n != n2:
        if line[n]:
            check += 1
        n += step
    # 가려는 곳이 빈경우와 아닌경우
    # 가려는 곳과 시작점 사이에 카드가 있는 경우와 아닌경우 
    # 가려는 곳이 보드 끝인 경우와 아닌경우 
    if line[n2]:         
        if check:
            #(0'1'2),(0'1'3),(0'2'3),(0'1''2'3),(1'2'3)
            number += check+1
        else:
            #(01)(02)(03)(12)(13)(23)
            number += 1
    else:
        if check:
            #(0'1'3)
            if (n2 == n1+3*step) and line[n2-2*step] and not line[n-step]:
                number += 3
            #(0'1'2),(0'2'3),(0'1''2'3),(1'2'3)
            else:
                number += check+1 
        else:
            #(03)(13)(23)
            if n2 == len(line)-1 or n2 ==0:
                number += 1      
            #(01)(02)(12)
            else:
                number += abs(n2-n1)          
    return number


def controlNumber(c1,c2,board):
    x1,y1 = c1[0],c1[1]
    x2,y2 = c2[0],c2[1]
    xFirst = 0
    yFirst = 0
    
    # 세로 먼저 이동
    # 그러나 x값이 같다면 세로이동은 넘어간다.
    if x2 == x1:
        pass
    else:
        line = [board[i][y1] for i in range(len(board))] 
        xFirst += Number(x1,x2,line)
    # y값이 같다면 가로이동은 넘어간다.
    if y2 ==y1:
        pass
    else:    
        line = board[x2]
        xFirst += Number(y1,y2,line)    
    #가로 먼저 이동
    if y2 ==y1:
        pass
    else:
        line =  board[x1]
        yFirst += Number(y1,y2,line)
    if x2 == x1:
        pass
    else:  
        line = [board[i][y2] for i in range(len(board))]
        yFirst += Number(x1,x2,line) 
    
    answer = xFirst if xFirst < yFirst else yFirst
    
    return answer

def solution(board, r, c):
    answer = 9999999
    # 모든 가능한 경우의 수를 만든다.
    # 카드 종류를 담을 리스트
    card_list =[]
    # 종류마다 카드 위치를 담을 리스트(리스트[카드종류]=카드좌표리스트)
    card_positions = [[] for _ in range(7)]
    # 리스트들을 채운다.
    for row in range(len(board)):
        for column in range(len(board)):
           if board[row][column]:
               card_list.append(board[row][column])
               card_positions[board[row][column]].append([row,column])
    # 카드 종류 정리
    card_list = list(set(card_list))
    # 순열 생성
    tmp_orders = list(permutations(card_list))
    # 카드 위치가 카드마다 2종이므로 (0,1) 2개 원소에 대해서 중복조합 생성
    select = list(product([1,0], repeat = len(card_list)))
    # 모든 가능한 이동방법을 담을 리스트
    orders= []
    # 카드 종류 순열과 중복조합을 순서대로 하나씩 묶어 새로운 리스트를 만든다.
    for order in tmp_orders:    
        for s in select:
            neworder = []
            for i,k in enumerate(s):
                neworder.append([order[i],k])
            orders.append(neworder)
    # 가능한 모든 경우의 수에 대해서    
    for order in orders:  
        copyBoard = copy.deepcopy(board)
        number =0
        start = [r,c]
        # 이동방법에 따라 이동한다.
        for card in order:
            # 같은 종류의 카드는 반드시 같이 선택해야하므로 하나를 골랐으면 다른 하나를 골라야한다.
            selected_card_1 = card_positions[card[0]][card[1]]
            selected_card_2 = card_positions[card[0]][1 if card[1] == 0 else 0]
            # 만약 시작점과 처음 고를 카드가 같은 위치라면, enter 입력 한번만 하면 되므로 +1
            if start == selected_card_1:
                number +=1
            else:
                # 그외의 경우는 그곳 까지 이동한뒤 enter를 입력해야하므로
                number += controlNumber(start,selected_card_1,copyBoard)+1
            # 2번째 카드로 가서 enter 입력
            number += controlNumber(selected_card_1,selected_card_2,copyBoard)+1
            # 이제 두 카드는 사라졌으므로 
            copyBoard[selected_card_1[0]][selected_card_1[1]] = 0
            copyBoard[selected_card_2[0]][selected_card_2[1]] = 0
            # 2번째 카드의 위치에서 다시 시작
            start = selected_card_2
        #가장 작은 조작 횟수를 저장한다.
        if number < answer:
            answer = number 
        
    return answer

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r, c = 1, 0
print(solution(board, r, c))

board= [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r, c = 0, 1
print(solution(board, r, c))

        
# [[2, 0], [3, 0], [1, 1]]
        
#print(start, selected_card_1,selected_card_2)
    
    