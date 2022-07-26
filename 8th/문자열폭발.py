# 반복하여 폭발하는 문자열을 찾으면 오래걸린다 판단
# 한번에 폭발 후 남는 문자열을 찾아보려고 생각
# 처음 생각, 폭발 문자열이 나타나면, 제거하고 문자열을 이어 붙이는 방향으로-> 끊고 이어붙이는 횟수가 너무 많아서 시간초과
# 두번째 생각, 잇고 끊는게 너무 만다면, 문자열리스트는 그대로 두소 폭발한 문자열만 None으로 바꾸어 None 아닌 문자열만 출력 -> 그럼에도 폭발 문자열 탐색시간이 오래걸려서 시간초과
# 마지막, 스택을 사용하여, 출력할 문자열을 담으면서 필요해지면 꺼내서 폭발 시킴-> 붙이는 시간만(O(1)) 들어감/필요없는 문자열은 없으므로 탐색시간역시 짧음
# 문자열을 지나가며, 폭발 문자열이 나타나면 제거하고, 폭발 문자열에 속하지 않으면 output에 집어 넣는다. 이 때 output에 폭발 문자열이 생기면 또다시 제거하고....
# strstrstrboomboomboom
# strstbbstrboomboomboom, 와 같은 문자열에서 stb 뒤로는 어떤 문자가 오더라도 더이상 폭발 시키는 것이 불가능하므로 output에서 더이상 그 앞으로는 검사하지 않게한다.
import sys
sys.stdin = open('8th\\input','r')
string = list(sys.stdin.readline().strip())
boom_string = list(sys.stdin.readline().strip())
b_len = len(boom_string)
s_len = len(string)
# 폭발문자열의 순서를 나타내는 값 초기값은 0이다.
b_position = 0
# 폭발문자열의 시작 순서가 담길 리스트/ 이 리스트가 비게 되는 순간, output 에 담긴 문자들은 더이상 폭발 가능성이 없다
pre_b_positions = []
# 출력할 값
output=[]      
            
for i in range(len(string)):
    # 앞에서부터 문자열을 담는다. 이 output에는 출력할 문자열이 최종적으로 남게 된다.
    output.append(string[i])
    # 폭발 문자열은 한번에 다 같이 터지므로 들어온 문자열이 폭발 문자열과 순서가 일치하게 진행하다가 
    if string[i] == boom_string[b_position]:
        # 마지막 폭발 문자열과도 일치한다면 폭발 시킨다.
        if b_position == b_len-1:
            b_position = 0
            count = 0
            j = 0
            # output 에는 폭발할 수 있는 문자열만 남아있으므로 폭발 문자열 갯수만큼 꺼내면 된다.
            for _ in range(b_len):
                output.pop()
                j += 1
            # 문자열을 폭발 시킨뒤, 만약 앞에서 못 폭발시키고 남겨둔 문자열이 있다면, 그 문자열이 폭발 문자열과 어디까지 일치했는지 나타내는 값을 하나 꺼낸다.
            if pre_b_positions:
                b_position = pre_b_positions.pop()
            # 만약 그러한 값이 없다면, 새로 시작한다.
            else:
                b_position = 0
        # 일치하였으므로 다음으로 간다.
        else:
            b_position += 1
    # 일치하지 않고 다시 폭발 문자열의 시작이 나타나면, 폭발문자열 순서를 초기화 한다.
    elif string[i] == boom_string[0]:
        # 그리고 그 순서를 기억하게 pre_b_positions 에 담는다.
        pre_b_positions.append(b_position)
        b_position = 1
    # 만약 폭발 문자열의 순서와 맞지않으면서 폭발문자열의 첫문자도 아닌 문자가 들어온다면
    else:
        # 그 이전 문자열은 이제 더이상 폭발할 가능성이 없으므로, pre_b_position을 지워버리고, 폭발문자열 순서를 초기화 한다.
        pre_b_positions.clear()
        b_position = 0

if output:
    for s in output:
        print(s,end='')
else:
    print('FRULA')