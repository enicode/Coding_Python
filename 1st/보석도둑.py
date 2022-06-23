import sys
import heapq
sys.stdin = open('coding-study\\input.txt', "r")

    
n,k = map(int, sys.stdin.readline().split())
# 보석의 무게를 담을 최소힙
mHeapJewels = []
# 보석 가치를 담을 최대힙
vHeapJewels = []
# 가방 무게를 담을 최소힙
heapBags= []
valueSum = 0
# 보석의 무게를 담는다.(정확히 모르겠습니다.)
for _ in range(n):
    m,v = map(int, sys.stdin.readline().split())
    heapq.heappush(mHeapJewels, (m,v))
# 가방의 무게를 담는다.              
for _ in range(k):
    b = int(sys.stdin.readline())
    heapq.heappush(heapBags, b)
# 가방이 없거나 보석이 없을 때 까지
# 보석힙에서 꺼내서 가방힙에 담는다.   
while heapBags and (mHeapJewels or vHeapJewels):
    # 가장 무게가 가벼운 가방부터 순서대로 꺼낸다.
    bag = heapq.heappop(heapBags)
    # 더이상 가방에 담을 수 있는 보석이 없을 때까지 보석을 꺼내서 가치 최대힙에 담는다.
    while mHeapJewels:
        if mHeapJewels[0][0] <= bag:
            jewel = heapq.heappop(mHeapJewels)
            #최소힙이 기본이기 때문에 음수로 바꿔주면 최대힙 처럼 만들 수 있다.
            heapq.heappush(vHeapJewels, -jewel[1])
        else: break
    # 가방에 담을 수 있는 보석이 있다면 그 중 최대 가치를 담는다.
    if vHeapJewels:    
        value = heapq.heappop(vHeapJewels)
        valueSum += -value

print(valueSum)  
