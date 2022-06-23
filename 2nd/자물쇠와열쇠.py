# 열쇠와 자물쇠를 겹칠 수 있는 모든 경우의 수를 따진다.
def solution(key, lock):
    answer = False        
    keysize = len(key)
    # 열쇠를 회전 시킬수 도 있으므로, 회전 시킨 열쇠에 대해서도 모두 해본다.
    cw90 = [[0 for i in range(keysize)] for j in range(keysize)]
    cw180 = [[0 for i in range(keysize)] for j in range(keysize)]
    cw270 = [[0 for i in range(keysize)] for j in range(keysize)]
    for i in range(len(key)):
        for j in range(len(key)):
            cw90[i][j] = key[keysize-j-1][i] 
            cw180[i][j] = key[keysize-i-1][keysize-j-1]
            cw270[i][j] = key[j][keysize-i-1]
    # 넷중 하나라도 가능하면 True         
    answer = subsolution1(key,lock) or subsolution1(cw90,lock) or subsolution1(cw270,lock) or subsolution1(cw180,lock)

    return answer

# 상하 방향 모든 경우의 수를 만들어준다.
def subsolution1(key,lock):
    answer = False
    keysize = len(key)
    locksize = len(lock)
    #우선 키의 마지막행과 자물쇠의 첫행이 겹칠 때 부터 키의 첫행이 자물쇠의 첫행과 겹치기 직전까지
    for i in range(1,keysize):
        #겹칠수 있는 열쇠부분
        keypart = key[-i:]
        #열쇠부분과 겹칠 수 있는 자물쇠 부분
        lockpart = lock[:i]
        # 남은 자물쇠 부분
        leftpart = lock[i:]
        # 남은 부분에 홈이 있으면 안됨
        check = True
        for line in leftpart:
            if 0 in line:
                check =False
                break
        # 겹쳐진 부분과 남은 부분이 모두 채워졌는지 확인한다.
        answer = check and subsolution2(keypart,lockpart)
        # 그렇다면 True 반환하고 종료
        if answer :
            return answer
    # 자물쇠 첫행이 열쇠 첫행과 겹칠 때부터 자물쇠의 마지막행과 키의 마지막행 이 겹치기 직전 까지
    for i in range(locksize-keysize+1):
        keypart = key
        lockpart = lock[i:keysize+i]
        # 이경우는 남는 부분이 2군데 이다.
        # 아래쪽과 위쪽
        leftpartDown = lock[keysize+i:]
        leftpartUp = lock[:i]
        check = True
        for line in leftpartUp:
            if 0 in line:
                check =False
                break
        for line in leftpartDown:
            if 0 in line:
                check =False
                break
        answer = check and subsolution2(keypart,lockpart)
        if answer :
            return answer
    # 자물쇠의 마지막행이 열쇠의 맨 아래에서 두번째 행과 겹칠 때부터 끝까지
    for i in range(1,keysize):
        keypart = key[:keysize-i]
        lockpart = lock[locksize-keysize+i:]
        leftpart = lock[:locksize-keysize+i]
        check = True
        for line in leftpart:
            if 0 in line:
                check =False
                break
        answer = check and subsolution2(keypart,lockpart)
        if answer :
            return answer
    return answer

#좌우 방향 모든 경우의 수를 체크 한다.
def subsolution2(keypart, lockpart):
    height = len(lockpart)
    width = len(keypart[0])
    lockwidth= len(lockpart[0])
    answer = False 
    for i in range(1,width):
        newkeypart=[]
        for keypartline in keypart:
            newkeypart.append(keypartline[-i:])
        newlockpart = []
        for lockpartline in lockpart:
            newlockpart.append(lockpartline[:i])
        leftpart=[]
        for leftpartline in lockpart:
            leftpart.append(leftpartline[i:])
        check = True
        for line in leftpart:
            if 0 in line:
                check =False
                break
        answer = check and subsolution3(newkeypart,newlockpart)
        if answer :
            return answer
    # 좌우는 행 대신 열을 처리
    for i in range(lockwidth-width+1):
        newkeypart = keypart
        newlockpart = []
        for lockpartline in lockpart:
            newlockpart.append(lockpartline[i:i+width])
        # 잘라내고 남은 부분에 1 이 있나 알려주는 알려주는 지표
        check = True     
        leftpartLeft=[]
        leftpartRight=[]
        # 처음에는 왼쪽으로 남는 것은 없다. 
        if i == 0 :
            pass
        else:
            for k in range(height):
                leftpartLeft.append(lockpart[k][:i])
        # 마지막엔 오른쪽으로 남는 것이 없다. 
        if i == lockwidth-width:
            pass
        else:
            for k in range(height):
                leftpartRight.append(lockpart[k][i+width:])
        if leftpartLeft:      
            for left in leftpartLeft:
                if 0 in left:
                    check = False
                    break
        if leftpartRight:
            for right in leftpartRight:
                if 0 in right:
                    check = False
                    break
        answer = check and subsolution3(newkeypart,newlockpart)
        if answer :
            return answer
    
    for i in range(1,width):
        newkeypart = []
        for keypartline in keypart:
            newkeypart.append(keypartline[:width-i])
        newlockpart = []
        for lockpartline in lockpart:
            newlockpart.append(lockpartline[lockwidth-width+i:])
        leftpart=[]
        for leftpartline in lockpart:
            leftpart.append(leftpartline[:lockwidth-width+i])
        check = True
        for line in leftpart:
            if 0 in line:
                check =False
                break        
        answer = check and subsolution3(newkeypart,newlockpart)
        if answer :
            return answer
        
    return answer

# 들어온 부분들이 맞는지 안맞는지 알려주는 것
def subsolution3(keypart, lockpart):
    answer = True
    for i in range(len(keypart)):
        for j in range(len(keypart[0])):
            if not keypart[i][j]^lockpart[i][j]:
                return False
    return answer
    


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock =[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))
'''
key = [[1, 0, 0], [0, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

key = [[0, 0, 0], 
       [1, 0, 1], 
       [0, 1, 0]]
lock = [[0, 1, 1, 1], 
        [1, 1, 1, 1], 
        [1, 0, 1, 0],
        [1, 1, 0, 1]]
'''