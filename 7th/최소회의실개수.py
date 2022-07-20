# 회의가 가장 빨리 끝나는 방의 끝나는 시간보다 시작하는 시간이 이르다면, 새로운 방이 필요하다. 
# 아니라면, 가장 빨리 회의가 끝나는 방에서 회의를 하면 되므로, 가장 빨리 회의가 끝나는 방의 회의 끝나는 시간을 바꿔준뒤, 다시 최소힙에 넣는다.
import sys
import heapq
sys.stdin = open('7th\\iuput','r')
N = int(sys.stdin.readline().strip())
# 회의 시작시간을 기준으로 하는 최소힙
meeting_q = []
for _ in range(N):
    heapq.heappush(meeting_q, list(map(int, sys.stdin.readline().split())))
#회의 끝나는 시간을 기준으로 하는 최소힙
room_q = [0]
while meeting_q:
    start = meeting_q[0][0]
    first_end = room_q[0]
    if start >= first_end:
        heapq.heappop(room_q)
        heapq.heappush(room_q, heapq.heappop(meeting_q)[1])
    else:      
        heapq.heappush(room_q, heapq.heappop(meeting_q)[1])

print(len(room_q))

