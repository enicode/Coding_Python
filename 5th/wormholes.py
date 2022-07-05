# 12개 이므로 완전탐색 해본다.
# 모든 경우의 수
# 중복 없이 웜홀을 2개씩 짝짓는 방법: 웜홀에 번호를 매긴다. 번호가 커지는 순으로만 짝을 짓는다.
import sys

sys.stdin = open("5th\\input","r")
N = int(sys.stdin.readline())
wormhole_list=[]

for _ in range(N):
    wormhole_list.append(list(map(int, sys.stdin.readline().split())))
# 어떤 웜홀끼리 페어인지 담을 리스트
pair =[-1 for _ in range(N)]
# 어떤 웜홀에서 나와서 +x 방향으로 걸어가면 다음으로 들어가게 되는 웜홀 리스트
nxt_hole= [-1 for _ in range(N)]   

#nxt 웜홀을 완성한다.
for i in range(N):
    min_x_diff = 1000000001
    for j in range(N):
        # 자기자신이 아니고 자기보다 -x 방향에 있는 웜홀이 아닌 웜홀들 중에서
        if wormhole_list[i][1] != wormhole_list[j][1]:
            continue
        if wormhole_list[i][0] >= wormhole_list[j][0]:
            continue
        diff = wormhole_list[j][0] - wormhole_list[i][0]
        # 최소 거리만큼 떨어진것이 nxt_hole
        if diff < min_x_diff:
            min_x_diff = diff
            nxt_hole[i] = j

def solution(pair,nxt_hole):
    # 결과
    result = 0
    # 몇번째 웜홀까지 페어가 있나 확인할 변수
    num = 0
    for i in range(N):
        # 만약 페어가 없는 경우가 있다면 아래 for문으로 간다.
        if pair[i] == -1:
            num =i 
            break
    else:
        # 만약 모두 페어가 있다면, 무한루프가 되는지 확인하여 되면 1 안되면 0을 반환한다.    
        if loop(pair,nxt_hole): 
            return 1
        else: return 0
    # 페어가 없는 웜홀 다음 웜홀부터 시작하여    
    for j in range(num+1,N):
        # 페어가 없는 웜홀은 num에 해당하는 웜홀과 페어를 시킨다.
        if pair[j] == -1:
            pair[num] = j
            pair[j] = num
            result += solution(pair, nxt_hole)
            # 위와 같은 페어에 대해서 결과를 얻었으므로 페어링을 초기화 한다.
            pair[num] = -1
            pair[j] = -1
    return result

def loop(pair, nxt_hole):
    # 모든 웜홀에 대해서 
    for start in range(N):
        # 처음 웜홀을 탈 위치는 그 웜홀이다.
        position = start
        # 모든 웜홀 숫자만큼 웜홀을 타본다.  
        for _ in range(N):
            # 다음 웜홀을 탈 위치는 nxt_hole 이다.
            position = nxt_hole[position]
            # 만약 nxt_hole이 없는 웜홀로 나왔다면 탈출한다.
            if position == -1 : break
            # 웜홀을 탄다.
            position = pair[position]
        # 이후에 탈출할수 없엇다면, loop 이므로 True 반환 아니면 False 반환
        if position != -1: return True
    return False

print(solution(pair, nxt_hole))
        




        