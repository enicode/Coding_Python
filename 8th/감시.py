# 4^8 =65536 완전탐색
import sys
import copy
sys.stdin = open('8th\input','r')
N, M = map(int, sys.stdin.readline().split())

office = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cameras= []
for i in range(len(office)):
    for j in range(len(office[i])):
        ct = [1,2,3,4,5]
        if office[i][j] in ct:
            cameras.append([[i,j],office[i][j]])

def monitor(o, cp, ct, d):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    office = o
    if ct == 1:
        y,x = cp
        while True: 
            x += dx[d]
            y += dy[d]
            if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                break
            if office[y][x] == 6:
                break
            if office[y][x] in [1,2,3,4,5]:
                pass
            else:
                office[y][x] = '#'
    elif ct == 2:
        ds = [d, (d+2)%4]
        for i in ds:
            y,x = cp
            while True: 
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                    break
                if office[y][x] == 6:
                    break
                if office[y][x] in [1,2,3,4,5]:
                    pass
                else:
                    office[y][x] = '#'
    elif ct == 3:
        ds = [d, (d+3)%4]
        for i in ds:
            y,x = cp
            while True: 
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                    break
                if office[y][x] == 6:
                    break
                if office[y][x] in [1,2,3,4,5]:
                    pass
                else:
                    office[y][x] = '#'        
    elif ct == 4:
        ds = [d, (d+2)%4,(d+3)%4]
        for i in ds:
            y,x = cp
            while True: 
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                    break
                if office[y][x] == 6:
                    break
                if office[y][x] in [1,2,3,4,5]:
                    pass
                else:
                    office[y][x] = '#'
    else:
        ds = [d,(d+1)%4,(d+2)%4,(d+3)%4]
        for i in ds:
            y,x = cp
            while True: 
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or y > len(office)-1 or x > len(office[y])-1:
                    break
                if office[y][x] == 6:
                    break
                if office[y][x] in [1,2,3,4,5]:
                    pass
                else:
                    office[y][x] = '#'
    return office
                
def solution(o, cs, count):
    answer = N*M
    office = o   
    directions = [0,1,2,3]
    if not cs:
        answer = 0
        for line in office:
            answer += line.count(0)
        return answer
    for d in directions:
        original = copy.deepcopy(office)
        office = monitor(office, cs[0][0], cs[0][1], d)
        others = cs[1:]
        answer = min(answer, solution(office, others,count+1))
        office = original
    return answer
        
print(solution(office,cameras,0))