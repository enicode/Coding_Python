import sys
sys.stdin = open('coding-study\\input.txt', "r")

n,k = map(int, sys.stdin.readline().split())
#numberList[value] = value 만드는데 들어가는 최소 동전의 갯수
coinList = []
valueList = []
numberList = [-1 for _ in range(k+1)]
for _ in range(n):
    coinList.append(int(sys.stdin.readline()))
#동전의 가치를 오름차순 정렬  
coinList.sort()
# 가치가 k를 넘는 동전 제거
for i,coin in enumerate(coinList):
    if coin>k:
        coinList = coinList[:i]
# 초기값 넣기
numberList[coinList[0]] = 1
valueList.append(coinList[0])
# k 까지 다음과 같은 연산을 반복한다.
for value in range(valueList[0]+1,k+1):
    # 동전의 최소 가치가 1이고 최소 value 개의 동전이 있다면 vlaue를 만들 수 있다.
    # 따라서 만들 수 있는 가치라면 아래 값보다는 적게 동전이 필요하다.
    min = value+1
    # 코인의 가치와 같은 가치는 하나의 동전으로 만들 수 있다.
    if value in coinList:
        valueList.append(value)
        numberList[value] = 1
    else:
        # 어떤 가치를 만들 때 필요한 동전의 최솟값은
        # (어떤가치 - 동전의 가치)를 만들 때 필요한 동전 갯수의 최솟값 +1 이다.
        for coin in coinList:
            # 만약 가치 - 동전의 가치가 만들 수 있는 값이라면
            if numberList[value-coin] !=-1:
                # 최솟값과 비교하여 최솟값을 구한다.
                if min > numberList[value-coin]+1:
                    min = numberList[value-coin]+1
        # 최솟값이 존재한다면 만들수 있는 가치 리스트에 가치를 넣고, 그때 필요한 동전의 최솟값도 기록한다.
        if min != k+1:
            valueList.append(value)
            numberList[value] = min
print(numberList[k])
