import sys
sys.stdin = open('7th\iuput','r')

# 기어를 돌리는 함수(g는 현재 기어 상태, d는 돌릴방향 1은 시계방향, -1은 반시계 방향, 돌리고 난뒤 기어 상태를 반환)
def rotate(g,d):
    gear = [None for _ in range(len(g))]
    if d == 1:
        for i in range(len(g)):
            gear[i] = g[i-1]
        return gear
    elif d == -1:
        for i in range(len(g)):
            gear[i] = g[(i+1)%8]
        return gear
# 기어의 정보를 리스트로 받는다.
g1=[int(pole) for pole in sys.stdin.readline().strip()]
g2=[int(pole) for pole in sys.stdin.readline().strip()]
g3=[int(pole) for pole in sys.stdin.readline().strip()]
g4=[int(pole) for pole in sys.stdin.readline().strip()]

# 기어를 K번 돌린다.
K = int(sys.stdin.readline())
for _ in range(K):
    # 기어 사이가 연결되었는지 알려줄 값
    connected12 = g1[2]^g2[6]
    connected23 = g2[2]^g3[6]
    connected34 = g3[2]^g4[6]
    n, d = map(int, sys.stdin.readline().split())
    # n 이들어오면 n번부터 돌린다.
    if n == 1:
        g1 = rotate(g1,d)
        if connected12:
            g2 = rotate(g2,-d)
            if connected23:
                g3 = rotate(g3,d)
                if connected34:
                    g4 = rotate(g4,-d)
    elif n == 2:
        g2 = rotate(g2,d)
        if connected12:
            g1 = rotate(g1,-d)
        if connected23:
            g3 = rotate(g3,-d)
            if connected34:
                g4 = rotate(g4,d)
    elif n == 3:
        g3 = rotate(g3,d)
        if connected23:
            g2= rotate(g2,-d)
            if connected12:
                g1 = rotate(g1,d)
        if connected34:
            g4 = rotate(g4,-d)
        
    else:
        g4 = rotate(g4,d)
        if connected34:
            g3 = rotate(g3,-d)
            if connected23:
                g2 = rotate(g2, d)
                if connected12:
                    g1 = rotate(g1, -d)
#조건에 맞게 출력한다.
print(g1[0] + 2*g2[0] + 4*g3[0] + 8*g4[0])