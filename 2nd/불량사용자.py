#모든 경우의 수를 따져야 한다.
import copy

def solution(user_id, banned_id):
    # 기본적으로 한 경우는 있다
    answer = 1
    # 밴아이디와 매치될 수 있는 모든 유저아이디를 2차원 리스트로 만든다.(딕셔너리로하면 밴아이디가 겹칠경우가 있어서 안됨)
    matchList = [['name',[]] for _ in range(len(banned_id))]
    for i,bId in enumerate(banned_id):
        for uId in user_id:
            # 우선 가능하다고 가정하고
            match = True              
            if len(bId) == len(uId):
                # 같지 않은것이 나올때까지, 단 *이면 판단하지 않는다. 나오지 않으면 그대로 TRUE 아니면 False
                for k in range(len(bId)):
                    if bId[k] == '*':
                        pass
                    else:
                        if bId[k]!=uId[k]:
                            match = False
                            break
            # 아이디의 길이가 같지 않으면 False
            else:
                match = False
            # 리스트에 추가해준다.
            if match:
                matchList[i][0] = bId
                matchList[i][1].append(uId)
    # 가능한 뽑을 수 있는 모든 경우의 수를 담은 리스트(단, 순서 상관 있게 담김)
    multiList = subsolution(matchList)
    for mmlist in multiList:
        # 리스트의 뽑힌 순서를 지운다.
        mmlist.sort()
    # 다시 정렬한다. 이제 중복된 리스트는 인접해 있다.         
    multiList.sort()

    # 중복된리스트를 지우고, 중복되지 않은 리스트가 나올때 마다 하나씩 늘린다./ 초기값이 1인 이유.
    for i in range(len(multiList)-1):
        if multiList[i] != multiList[i+1]:
            answer += 1
                       
    return answer

# 처음 리스트에서 유저아이디를 뽑고 뽑은 아이디는 다른 리스트에서 제거하고를 반복하여 유저리스트를 만들어주는 재귀함수
def subsolution(matchList):
    # 가능한 유저리스트를 담는 리스트
    nlist = []
    # 만약 하나의 리스트만 들어오면 뽑을수있는 모든 경우의 수를 각각 담은 리스트를 반환한다.
    if len(matchList) == 1:       
        for mlist in matchList: 
            for el in mlist[1]:
                nlist.append([el])
        return nlist
    # 첫 그룹 아이디중 하나를 다른 곳에선 있다면 삭제
    # 이것을 모든 그룹내 아이디에서 반복
    for i in range(len(matchList[0][1])):
        # 재귀함수에 넣어줄 새로운 매치리스트
        newMatchList = copy.deepcopy(matchList)
        # 이제 첫그룹을 제외한 모든 그룹에서
        for k in range(1,len(matchList)):
            # 선택한 아이디와 같은 아이디가 발견되면 삭제한다.
            if matchList[0][1][i] in newMatchList[k][1]:
                newMatchList[k][1].remove(matchList[0][1][i])
        #위 과정을 첫 그룹을 제외하고 반복한다.    
        tmp2 = subsolution(newMatchList[1:])
        # 그렇게 해서 구한 리스트들에 대해서
        for e in tmp2:
            # 아까 뽑은 아이디를
            tmp = [matchList[0][1][i]]
            # 리스트에넣는다.(1차원배열)
            tmp.extend(e)
            # 그리고 반환할 리스트에 추가한다.(2차원배열)
            nlist.append(tmp)
    # 그렇게 만든 리스트를 반환한다.
    return nlist

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
ban_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id,ban_id))