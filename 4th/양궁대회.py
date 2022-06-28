# 2^11 ~ 2000 완전탐색       
from itertools import product

def solution(n, info):
    answer = [n,0,0,0,0,0,0,0,0,0,0]
    # 점수를 획득하는 경우를 1 아닌 경우를 0 으로 하여 10번 중복뽑기
    cases = product([1,0],repeat = 10)
    # 가능한 모든 과녁 명중 리스트들을 모은 리스트
    p_answers =[]
    for case in cases:
        # 과녁 명중 리스트
        p_answer = [0 for _ in range(11)]
        left_arrow = n
        for i,p in enumerate(case):
            # 그 과녁의 점수를 얻고 싶다면
            if p :
                # 어피치가 쏜 화살보다 한 발 많이 쏴야한다.(최적)
                if info[i] < left_arrow :
                    left_arrow -= info[i]+1
                    p_answer[i] = info[i]+1
                else:
                    #만약 그럴수 없다면 이 리스트는 폐기
                    break
        # 마친 뒤 남은 화살은 0점에 다 쏜다.
        else:          
            if left_arrow:
                p_answer[-1] += left_arrow
            # 리스트에 추가
            p_answers.append(p_answer)
    
    diff_list = []
    # 라이언의 점수와 어피치의 점수차이를 리스트로 만들어서 최댓값을 구해보고 0보다 작거나 같으면 -1을 반환한다.      
    for p_answer in p_answers:
        lpoint = sum([10-i if p_answer[i] else 0 for i in range(11)])
        apoint = sum([10-i if not p_answer[i] and info[i] else 0 for i in range(11)])
        diff_list.append(lpoint -apoint)
    m_point = max(diff_list)
    if m_point <= 0:
        return [-1]  
    #최댓값을 쏠수 있는 경우가 여러가지 있을 수 있기 때문에 
    for i,diff in enumerate(diff_list):
        # 최댓값을 쏘는 모든 경우들 마다 
        if diff == m_point:
            for k in range(11):
                # 큰 점수를 더 적게 쏘는 경우가 있다면 그 경우로 교체 해야한다.
                if answer[10-k] < p_answers[i][10-k]:
                    answer = p_answers[i]
                # 같다면 다음 비교를 위해 넘어가고
                elif answer[10-k] == p_answers[i][10-k]:
                    pass
                # 크다면 바꾸지 않고 비교를 중단한다.
                else:
                    break

    return answer

    
    


n = 7	
info = [3,1,1,1,1,0,0,0,0,0,0]
print(solution(n,info))
n = 1	
info = [1,0,0,0,0,0,0,0,0,0,0]
print(solution(n,info))
n = 9	
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n,info))
n = 10	
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n,info))