import sys
# 소리를 왼쪽, 오른쪽에서 자르거나 붙이기 쉽게
from collections import deque
import copy
sys.stdin = open('7th\iuput', 'r')
# 100~1~ 을 1번 소리, 01 을 2번 소리라고 하자
# 그리고 1번 소리에서 맨 앞 1을 '1번 소리의 시작하는 1', 중간에 있는 ~ 를 1번 소리의 중간 부분, 마지막에 있는 ~ 부분을 1번 소리의 마지막 부분이라고 하자.
# 1번 소리는 가변적인 소리이므로 이렇게 나눠주고, 2번소리는 그렇지 않으므로 그냥 2번 소리라고만 구분한다.  

# 1번소리와 2번 소리 모두 1로 끝나므로, 잠수함 소리이려면 반드시 1로 끝나는 소리여야한다. 
# 그러나 1로 끝나는 소리라고 하여도 1번 소리와 2번 소리 중 어느것으로 끝나는지는 알수 없다.
# 따라서 뒤에서 부터 앞으로 가면서 가능한 모든 경우의 수를 따져가며, 소리의 처음까지 거슬러 올라갈 때 단 하나의 모순없는 경우라도 있다면, 잠수함소리라고 판단하고, 
# 거슬러 올라가면서 모순없이 더이상 거슬러 올라갈 수 있는 경우의 수가 없을 때, 잡음 으로 판단한다.

# 소리를 재귀적으로 거슬러 올라가면서 잠수함 소리일 수도 있는지 알려주는 함수
# sl은 남은 거슬러 올라가야할 소리, sr은 지금까지 거슬러 온 소리, d는 지금 들어온 소리를 1번 소리와 2번 소리의 어느 부분으로 생각하고 판단할지 알려주는 식별자
# 1001011010 101
def possible(sl,sr,d):
    answer = False 
    # 깊은 복사로 서로 영향 미치지 않게 중간에 sl 에서 sr로 소리를 옮겨 판단해야 한다.
    l_string = sl.copy()
    r_string = sr.copy()
    # 이게 1번 소리와 2번 소리의 어느 부분에 해당할 수 있는지 식별해주는 값들의 리스트
    # 들어올 때는 하나의 식별자를 가질지라도 다음 거슬러 올라갈 소리에 대해서는 여러가능성이 있을수 있으므로 리스트로 한다.
    det = [d]
    # 이제 sl의 오른쪽에서 소리를 하나 떼어 본다.
    tmp = l_string.pop()
    # 만약 2번 소리로 판단하고 다음 소리를 구분해야한다면,( tmp를 판별해야할 소리라고 하자 ) 
    # 2번 소리는 반드시 0으로 시작해야하므로 판별해야할 소리가 0 이라면 그 뒤에 오는 소리는 반드시 1이어야만한다. 따라서
    # 01 이면 계속해서 2번 소리로
    # 00 이 오면 False 
    # 만약 판별해야할 소리가 1 이라면,
    # r_string[0] 값이 0이라면, 판별해야할 소리는 1번 소리의 마지막이고, 2번 소리가 시작하는 경우의 수가 하나 있고 혹은 2번 소리의 계속일 수도있다.
    # r_string[0] 값이 1이라면, 2번 소리는 11을 부분을 가질 수 없으므로 판별해야할 소리는 1번 소리의 마지막에 해당하는 1이다.
    # 11 이면 1번 소리의 마지막으로
    # 10 이면 2가지 가능성(2번 소리로 계속 갈지, 1번 소리의 마지막으로 갈아탈지)
    if det == [3]:
        if tmp:
            if r_string[0]:
                det = [2]
            else:
                det = [2,3]
        else:
            if r_string[0]:
                pass
            else:
                return False               
    # r_string[0]가 만약 1번 소리의 마지막 부분이라면 판별해야할 소리가 0 이라면 중간부분으로 가는 것이므로(반대로 1이면 계속 마지막부분 이다.)
    # 100~1~
    elif det == [2]:
        if not tmp:
            det = [1]
    #r_string[0]가 1번 소리의 중간 부분이라면 판별해야할 소리가 1 이라면 1번 소리를 시작하는 1이어야하므로 단, 0은 2개 이상 있어야한다. 100~ 이기 때문에 100은 되어도 10은 안됨
    elif det == [1]:
        if tmp and (list(r_string)[:2] == [0,0]):
            det =[0]
        elif tmp and not (list(r_string)[:2] == [0,0]):
            return False         
    #r_string[0] 가 1번 소리의 처음인 1 이라면
    else:
        # 판별해야할 소리가 0 이라면 0으로 끝나는 경우는 없기 때문에 False 반환
        if not tmp:
            return False
        # 만약 앞에 1이라면 처음시작과 마찬가지고 det 값을 2, 또는 3으로 가질 수 있다.
        else:
            det = [2,3]
    # 위와 같은 판별을 거쳤는데, 남은 거슬러 올라가야할 소리가 없다면
    if not l_string:
        # 마지막에(즉 소리의 처음에) det 값이 0이어서 1번 소리의 시작하는 1 이거나
        # det 값이 3 인데 판별하려는 소리가 0 이어서 2번 소리의 시작하는 0 이거나 해야한다.
        if det == [0] or (det == [3] and tmp == 0):
            return True
        else:
            return False
    #가능한 모든 경우의 수에 대해서
    for v in det:
        #det 값마다 deepcopy를 따로 하여 서로 영향을 미치지 않게
        new_r_string = copy.deepcopy(r_string)
        new_r_string.appendleft(tmp)
        new_l_string = copy.deepcopy(l_string)
        answer = answer or possible(new_l_string, new_r_string, v)
    return answer  
sounds = deque()
tmp = sys.stdin.readline().strip()
for i in range(len(tmp)):
    sounds.append(int(tmp[i]))
# 처음 판별해야할 소리
r_char = sounds.pop()
start_string = deque([r_char])
#끝 나는 숫자는 반드시 1이어야하고, 두번째 소리로 끝날수도 있고 첫번째 소리로 끝날수도 있으므로
if r_char == 1 and (possible(sounds,start_string,3) or possible(sounds,start_string,2)):
    print('SUBMARINE')
else:
    print('NOISE')
    
sound_list = ['1001', '01', '100001', '010101', '1000001110101', '1001110101', '0101010101', '10010110000001111101', '01010101011000111', '10000111001111']



