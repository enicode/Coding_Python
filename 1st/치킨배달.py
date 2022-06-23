import sys
sys.stdin = open('coding-study\\input.txt', "r")
# 집 리스트   
def Home(cityMap):
    return [[i,j] for i in range(len(cityMap)) for j in range(len(cityMap))if cityMap[i][j] == 1]
# 치킨집 리스트
def KFC(cityMap):
    return [[i,j] for i in range(len(cityMap)) for j in range(len(cityMap))if cityMap[i][j] == 2]
# 주어진 리스트(numberList)에서 m 개를 뽑는 조합(chosenList)을 반환하는 함수
def Combination(numberList,m,chosenList):
    newChosenList = []     
    if m == 0:
        return chosenList
    # 처음에는 종류 별로 다 골라야 함      
    if not chosenList:
        for number in numberList:
            newChosenList = [[i] for i in numberList]
    # 그 다음 부터는 존재 하는 리스트(chosenList)에 하나씩 숫자를 추가해서 새로운 리스트로 넣어줘야함
    for chosen in chosenList:
        # 그런데 그 때 추가할 수 있는 숫자는 존재하는 리스트의 가장 큰 숫자보다 커야만 함
        for number in range(chosen[-1]+1, numberList[-1]+1):
            newChosen = chosen.copy()
            newChosen.append(number)
            newChosenList.append(newChosen)
    
    newChosenList = Combination(numberList, m-1, newChosenList)
             
    return newChosenList       
# [치킨집, 집 , 치킨거리]리스트 와 jump(집 수)가 주어지면 도시치킨거리(ccd)를 반환 하는 함수    
def CCD(khdlist,jump):
    ccd = 0
    # 집으로 묶고, 거리로 오름차순 정렬
    khdlist.sort(key = lambda x : (x[1],x[2]))
    # 집마다 치킨 거리를 더한다.    
    for d in range(0,len(khdlist),jump):
        ccd +=  khdlist[d][2]
    return ccd

n, m = map(int, sys.stdin.readline().split())
cityMap = [None for _ in range(n)]
for i in range(n):
    cityMap[i]=list(map(int, sys.stdin.readline().split()))
              
kfcs= KFC(cityMap)    
numOfKFC = len(kfcs)
homes = Home(cityMap)
numOfHomes =len(homes)
khdlist = []

# [kfc,home,distance] 리스트를 만든다//KFC 기준으로 묶인 상태
for kfc in kfcs:
    for home in homes:
        khdlist.append([kfc,home,abs(home[0]-kfc[0])+abs(home[1]-kfc[1])])
        
# 폐업 해야할 치킨집 번호 조합을 고른다.           
closedKFCComb = Combination([i for i in range(numOfKFC)],numOfKFC-m,[])
# 대충 이보다 ccd가 클수는 없음
ccd = 2 * numOfHomes * len(cityMap)

# 폐업할 치킨집이 하나도 없다면 그대로 ccd를 출력한다.
if not closedKFCComb:
    print(CCD(khdlist,m))
else:
    # 모든 조합에 대해서 ccd를 구해보고 그 중 가장 짧은 값을 출력한다.
    for comb in closedKFCComb:
        # 폐업한 치킨집에 대한 정보가 없을 새로운 khdlist를 생성한다.
        newKhdlist = khdlist.copy()
        while comb:
            tmp =[]
            # 폐업할 치킨집 정보를 뒤에서부터 삭제하면 앞쪽 인덱스는 그대로
            tmp.extend(newKhdlist[:(comb[-1])*numOfHomes])
            tmp.extend(newKhdlist[(comb[-1]+1)*numOfHomes:])
            newKhdlist = tmp
            comb = comb[:-1]
        tmpccd = CCD(newKhdlist,m)
        if  tmpccd < ccd:
            ccd = tmpccd
    print(ccd)
