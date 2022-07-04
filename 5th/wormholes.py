# 12개 이므로 완전탐색 해본다.
# 모든 경우의 수
import sys

sys.stdin = open("5th\\input","r")
N = int(sys.stdin.readline())
wormhole_list=[]

for _ in range(N):
    wormhole_list.append(list(map(int, sys.stdin.readline().split())))
pair =[-1 for _ in range(N)]
nxt_hole= [-1 for _ in range(N)]   

for i in range(N):
    min_x_diff = 1000000001
    for j in range(N):
        if wormhole_list[i][1] != wormhole_list[j][1]:
            continue
        if wormhole_list[i][0] >= wormhole_list[j][0]:
            continue
        diff = wormhole_list[j][0] - wormhole_list[i][0]
        
        if diff < min_x_diff:
            min_x_diff = diff
            nxt_hole[i] = j

def solution(pair,nxt_hole):
    result = 0
    num = 0
    for i in range(N):
        if pair[i] == -1:
            num =i 
            break
    else:    
        if loop(pair,nxt_hole): 
            return 1
        else: return 0
        
    for j in range(num+1,N):
        if pair[j] == -1:
            pair[num] = j
            pair[j] = num
            result += solution(pair, nxt_hole)
            pair[num] = -1
            pair[j] = -1
    return result

def loop(pair, nxt_hole):
    for start in range(N):
        position = start
        for _ in range(N):
            position = nxt_hole[position]
            if position == -1 : break
            position = pair[position]
        if position != -1: return True
    return False

print(solution(pair, nxt_hole))
        




        