# 10만*5만>>1억
# 메모리를 더 써서 시간을 단축, 해시맵 
import bisect
def solution(info, query):
    answer = []
    infodict ={}
    # 딕셔너리 이름 만들기 '언어이름직군경력소울푸드'를 key로 성적을 value로 만든다.
    # 조건없이 탐색 하는 경우에도 대비하여 -도 포함
    for inf in info:
        l, g, c, sf, s = inf.split(" ")
        s = int(s)
        for i in range(2):
            ll = l if i == 0 else '-'
            for j in range(2):
                gg = g if j == 0 else '-'
                for k in range(2):
                    cc = c if k == 0 else '-'
                    for m in range(2):
                        sfsf = sf if m == 0 else '-'
                        try:
                            infodict[f'{ll}{gg}{cc}{sfsf}'].append(s)
                        except KeyError:
                            infodict[f'{ll}{gg}{cc}{sfsf}'] = [s]
    for values in infodict.values():
        values.sort()
                                                                 
    for request in query:
        l, g, c, sfas = request.split(" and ")
        sf, s = sfas.split(" ")
        s = int(s)
        string =f'{l}{g}{c}{sf}'
        #만약에 그러한 조건이 존재하면
        try: 
            #이진탐색하여 최소기준을 처음으로 넘는 값이 나오는 인덱스를 찾는다.
            index = bisect.bisect_left(infodict[string], s)
            answer.append(len(infodict[string])-index)
        #존재하지 않으면 0 
        except KeyError:    
            answer.append(0)

    return answer                  
            
        
info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info,query))


'''
info =["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
'''