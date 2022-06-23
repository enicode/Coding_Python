import sys
sys.stdin = open('coding-study\\input.txt', "r")

# 가능한 다음 맛을 알려주는 함수
# 딸기 우유 0, 초코우유 1, 바나나우유 2
def next(taste):
    nextTaste=[]
    if len(taste)>1:
        nextTaste.append((taste[0]+1)%3)
        nextTaste.append((taste[1]+1)%3)
    else:
        nextTaste.append((taste[0]+1)%3)
    return nextTaste
# 이 가게를 지나면 어떻게 되는지 알려주는 함수
def afterHere(countA,taste1,taste2):
    newCount = countA
    newTaste =  taste1
    if taste2 in taste1:
        newCount += 1
        newTaste = next([taste2])
       
    return newCount, newTaste 

size = int(sys.stdin.readline())
# 그 가게까지 마실수있는 최대 우유 갯수를 저장할 리스트
countMap = [[0 for _ in range(size)] for _ in range(size)]
# 가게에서 파는 우유 종류를 저장할 리스트
tasteMap = []
for _ in range(size):
    tasteMap.append(list(map(int, sys.stdin.readline().split())))
# 그 가게에서 우유를 마신다면 다음 우유의 맛은 어때야 하는지 알려주는 지도
nextTasteMap = [[0 for _ in range(size)] for _ in range(size)]
# 처음 마실 우유는 딸기우유다.
iTaste = 0
# 처음 우유 이후에는 마실수 있는 우유는 리스트로 받는다.
# 왜냐하면 북쪽에서 진입할 경우와 동쪽에서 진입할 경우, 2가지 맛이 있을 수도 있기 때문이다.
# 처음 가게가 마실 수 있는 우유를 판다면
if tasteMap[0][0] == iTaste:
    countMap[0][0] = 1
    nextTasteMap[0][0] = next([iTaste])
# 그렇지 않다면
else:
    nextTasteMap[0][0] = [iTaste]

# countMap과 nextTasteMap의 첫열 초기화
for south in range(1,size):
    # 지금 여기서 파는 우유 맛
    tasteHere = tasteMap[south][0]
    # 이 가게 바로 북쪽을 지난 다음에 마실수 있는 우유의 맛
    nextTasteNorth = nextTasteMap[south-1][0]
    # 이 가게 바로 북쪽까지 먹어온 우유의 갯수
    countNorth = countMap[south-1][0]
    # 만약 이곳에서 마실수 있는 우유를 판다면, 
    if tasteHere in nextTasteNorth:
        # 먹어온 우유의 갯수는 1 늘어나고
        countMap[south][0] = countNorth + 1
        # 다음 마실 우유의 맛은 여기서 마신 우유 다음 맛이 된다.
        nextTasteMap[south][0] = next(nextTasteNorth)
    else:
        # 아니면 바로 북쪽 값을 유지
        countMap[south][0] = countNorth
        nextTasteMap[south][0] = nextTasteNorth
# countMap과 nextTasteMap의 첫행 초기화
for east in range(1, size):
    tasteHere = tasteMap[0][east]
    nextTasteWest = nextTasteMap[0][east-1]
    countWest = countMap[0][east-1]
    if tasteHere in nextTasteWest:
        countMap[0][east] = countWest +1
        nextTasteMap[0][east] = next(nextTasteWest)
    else:
        countMap[0][east] = countWest
        nextTasteMap[0][east] = nextTasteWest
      
for south in range(1,size):        
    for east in range(1,size):
        tasteHere = tasteMap[south][east]
        # 북쪽경로에서 올 경우 마실수 있는 우유의 맛
        nextTasteNorth = nextTasteMap[south-1][east]
        # 서쪽경로에서 올 경우 마실수 있는 우유의 맛
        nextTasteWest = nextTasteMap[south][east-1]
        # 북쪽경로에서 올 경우 마셔온 우유의 갯수
        countNorth = countMap[south-1][east]
        # 서쪽경로에서 올 경우 마셔온 우유의 갯수
        countWest = countMap[south][east-1]
        # 이 가게를 북쪽경로로 통과할 경우 마신 우유의 갯수와, 다음 우유의 맛
        afterCountNorth, afterTasteNorth = afterHere(countNorth, nextTasteNorth, tasteHere)
        # 이 가게를 서쪽경로로 통과할 경우 마신 우유의 갯수와, 다음 우유의 맛
        afterCountWest, afterTasteWest = afterHere(countWest, nextTasteWest, tasteHere)
        # 북쪽이 서쪽보다 많이 마시게 된다면
        if afterCountNorth > afterCountWest:
            countMap[south][east] = afterCountNorth
            nextTasteMap[south][east] = afterTasteNorth
        # 서쪽이 북쪽보다 많이 마시게 된다면
        elif afterCountNorth < afterCountWest:
            countMap[south][east] = afterCountWest
            nextTasteMap[south][east] = afterTasteWest
        # 어떤 경로를 택해도 같다면
        else:
            tmpTaste=[]
            tmpTaste.extend(afterTasteNorth)
            tmpTaste.extend(afterTasteWest)
            # 서로 같은 맛이라면 중복되므로 제거
            tmpTaste = list(set(tmpTaste))
            # 둘 중 어느 것이어도 상관없음
            countMap[south][east] = afterCountNorth   
            nextTasteMap[south][east] = tmpTaste

print(countMap[size-1][size-1])