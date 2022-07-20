# 반복하여 폭발하는 문자열을 찾으면 오래걸린다.
# 한번에 폭발 후 남는 문자열을 찾아본다.
# 문자열을 지나가며, 폭발 문자열이 나타나면 제거하고, 폭발 문자열에 속하지 않으면 남은 문자열에 집어 넣는다. 이 때 검사한 문자열에서 폭발 문자열이 생기면 또다시 제거하고....
# 검사한 문자열을 수정한다.
import sys
sys.stdin = open('8th\\input','r')

string = sys.stdin.readline()

string_list = [string[i] for i in range(string)]