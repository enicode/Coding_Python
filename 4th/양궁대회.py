# 2^11 ~ 2000 완전탐색       
from itertools import product

def solution(n, info):
    answer = [n,0,0,0,0,0,0,0,0,0,0]
    cases = product([1,0],repeat = 10)
    lpoint = 0
    apoint = 0
    std = 0
    p_answers =[]
    for case in cases:
        p_answer = [0 for _ in range(11)]
        left_arrow = n
        for i,p in enumerate(case):
            # 그 과녁의 점수를 얻고 싶다면
            if p :
                # 어피치가 쏜 화살보다 한 발 많이 쏴야한다.
                if info[i] < left_arrow :
                    left_arrow -= info[i]+1
                    p_answer[i] = info[i]+1
                else:
                    break
        else:
            if left_arrow:
                p_answer[-1] += left_arrow
            p_answers.append(p_answer)
            
    for p_answer in p_answers:
        lpoint = sum([10-i if p_answer[i] else 0 for i in range(11)])
        apoint = sum([10-i if not p_answer[i] and info[i] else 0 for i in range(11)])
        diff = lpoint - apoint
        if diff > std:
            std = diff
    if std <= 0:
        return [-1]
    
    for p_answer in p_answers:
        lpoint = sum([10-i if p_answer[i] else 0 for i in range(11)])
        apoint = sum([10-i if not p_answer[i] and info[i] else 0 for i in range(11)])
        diff = lpoint - apoint
        if diff == std:
            for i in range(11):
                if answer[10-i] < p_answer[10-i]:
                    answer = p_answer
                elif answer[10-i] == p_answer[10-i]:
                    continue
                else:
                    break
    return answer

    
    


n = 7	
info = [3,1,1,1,1,0,0,0,0,0,0]
#print(solution(n,info))
n = 1	
info = [1,0,0,0,0,0,0,0,0,0,0]
print(solution(n,info))
n = 9	
info = [0,0,1,2,0,1,1,1,1,1,1]
#print(solution(n,info))
n = 10	
info = [0,0,0,0,0,0,0,0,3,4,3]
#print(solution(n,info))