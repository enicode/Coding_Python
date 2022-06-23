import sys
sys.stdin = open('coding-study\\input.txt', "r")
# 옆 아이와 키 차이를 반환하는 함수
def HDiffs(groups):
    diffs=[]
    for i in range(1,len(groups)):
        diffs.append(groups[i]-groups[i-1])
    return diffs

n,k = map(int, sys.stdin.readline().split())

# 키를 받아서 리스트로 만든다.(이미 정렬된 상태)
heights = list(map(int, sys.stdin.readline().split()))
# 키 리스트를 옆 사람과 키차이 리스트로 만든다.
hDiffs = HDiffs(heights)
# 키 차이를 오름차순으로 정렬한다.
hDiffs.sort()
# hDiff는 이미 키가 정렬 된 상태에서 n 번째 값과 n+1 번째 값의 차이를 계산하여 오름차순 정렬한 것이므로
# 만약 조를 2개로 나눈다면, hDiff[0]가 비용이 된다.
# 왜냐하면 원생 1...N이 오름차순 정렬되어있으므로 (1...a)<-hDiff[0]->(a+1...N)이 최적해이기 때문이다. 
# 따라서 k 개의 조로 나누려면 hDiff[0] 부터 hDiff[n-k-1]까지 합이 최소 비용이 된다.
print(sum(hDiffs[:n-k]))

