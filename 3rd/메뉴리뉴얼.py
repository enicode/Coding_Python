def solution(orders, course):
    answer = {} 
    combinations = {}
    # 코스에 포함될 요리 숫자를 key로 코스요리를 value로 하여 딕셔너리 생성
    for number in course:
        combinations[number] = []
    # 가능한 모든 코스 요리 조합을 추린다. (모든 주문과 모든 코스요리 숫자에 대해서)
    for order in orders:
        for number in course:
            # 주문한 요리 수가 만들 코스 요리의 요리 숫자보다 많거나 같은경우에만 가능하다.
            if len(order) >= number:
                types = C(order,number,[])
                # 모든 조합에 대해서
                for c in types:
                    #딕셔너리에 추가한다.
                    if not c in combinations[number]:
                        combinations[number].append(c)
    # n개의 요리로 구성된 코스 요리가 새로운 매뉴에 포함되면
    # n개의 요리로 구성된 코스 요리로 만들수 있는 모든 다른 조합의 코스요리를 삭제한다.
    # 그런데 만약 삭제해야할 코스 요리중에서 원래 코스요리보다 주문을 같거나 많이한게 있다면 살린다.
    for number in combinations:
        for c1 in combinations[number]:
            #이름순 정렬
            c1.sort() 
    # 리스트로 있는 코스 요리를 문자열 형태로 바꿈
    for number in combinations:
        tmp = []
        # 코스요리숫자 별 가능한 코스 요리에 대해서
        for value in combinations[number]:
            # 글자 단위로 분해된 코스 요리를 합쳐줌
            newcourse = ""      
            for menu in value:
                newcourse = newcourse + menu
            tmp.append(newcourse)
        combinations[number] = tmp
    
    #삭제할 목록
    dellist = []
    #코스요리 숫자마다
    for number in course:
        max = 2
        #만들어진 코스 요리종류에 대해서
        for order in combinations[number]:
            # 제일 흔하게 주문한 코스요리를 찾는다.
            if NOO(orders,order) > max:
                max = NOO(orders,order)
        for order in combinations[number]:
            # 제일 흔하게 주문한 요리조합과 같은 빈도로 주문한 요리조합 찾는다.
            if NOO(orders,order) == max:
                answer[order] = NOO(orders,order)
                                             
    # 가능한 모든 코스요리에 대해서         
    for orderkey in answer:
        for tt in C(orderkey, len(orderkey)-1,[]):
            # 분해한 코스요리가 코스요리보다 적거나 같게 주문 되었으면 삭제한다
            if answer[tt] <= answer[orderkey]:
                dellist.append(tt)
    
    
     
    dellist = list(set(dellist))
    for delitem in dellist:
        del answer[delitem]
    answer = list(answer.keys())
    answer.sort()
    return answer


#중복된 주문의 갯수를 반환해줌
def NOO(orders,order):
    numberOfOrder = 0
    # 그 주문을 제외한 모든 주문들 중에
    for otherOrder in orders:
        # 그 주문을 포함한 주문이 있는지 확인한다.
        for menu in order:
            if not menu in otherOrder:
                break
        else:
            #있다면 1 증가, 자기 자신도 검사하므로 1은 반드시 넘음
            numberOfOrder += 1
    
    return numberOfOrder    

#조합함수    
def C(order,number,menulist):
    newList = []
    if number == 0:
        return menulist
    # 처음에는 종류 별로 다 골라야 함      
    if not menulist:
        for menu1 in order:
            newList = [[menu1] for menu1 in order]
    # 그 다음 부터는 존재 하는 리스트(menulist)에 하나씩 메뉴를 추가해서 새로운 리스트로 넣어줘야함
    for chosen in menulist:
        # 그런데 그 때 추가할 수 있는 요리의 번호는 1 큰 것부터 가능
        for menu2 in order[order.index(chosen[-1])+1:]:
            newChosen = chosen.copy()
            newChosen.append(menu2)
            newList.append(newChosen)
    newList = C(order, number-1, newList)
    return newList
        

order = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
    
print(solution(order,course))