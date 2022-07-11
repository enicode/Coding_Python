# 외판원 문제 변형 + 플로이드 워셜 알고리즘  
import sys

INF = float('inf')
N, K = map(int, sys.stdin.readline().split())
# 10000-1 = 1111, 비트마스크
end = (1<<N)-1
cache = [[None]*(1<<N) for _ in range(N)]
time_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 플로이드-와셜
for m in range(N):
    for s in range(N):
        for e in range(N):
            time_board[s][e]  = min(time_board[s][e], time_board[s][m] + time_board[m][e])

#외판원
def solution(cur, visited):
    # 모두 방문 하였으면 더 이상 시간비용이 들지 않으므로 0을 반환
    if visited == end:
        return 0
    # 방문하지 않은 곳이 있다면,
    # 또한 현재 위치에서 시작하여 방문하지 않은 곳들을 모두 방문하는데 필요한 최소시간경로가 이미 존재한다면, 
    if cache[cur][visited] is not None:
        # 그 값을 반환한다.
        return cache[cur][visited]
    cache[cur][visited] = INF
    # 모든 행성들 중
    for nxt in range(N):
        # 다음 행성이 될 수 있는 행성들에 대해(방문 안한 모든 행성들에 대해)
        if (1<<nxt) & visited == 0 :
            # (지금 행성에서 다음 행성까지 시간 + 다음 행성에서 다른 모든 행성을 도는 데 걸리는 시간) 의 최솟값을 찾는다. 
            cache[cur][visited] =min(cache[cur][visited], time_board[cur][nxt] + solution(nxt, visited | (1 << nxt)))
    return cache[cur][visited]

print(solution(K, 1 << K))