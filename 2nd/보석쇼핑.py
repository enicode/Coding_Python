'''
def solution(gems):
    answer = []
    gemDict = {}
    lastGems = []
    minLength = len(gems)
    for i,gem in enumerate(gems):
        if not gem in gemDict:
            minLength = len(gems)
            gemDict[gem] = i+1
            lastGems.append(i+1)
        else:
            lastGems.remove(gemDict[gem]) 
            gemDict[gem] = i+1
            lastGems.append(i+1)
        section = [lastGems[0],lastGems[-1]]
        length = lastGems[-1]-lastGems[0]
        if minLength > length:
            minLength = length
            answer = section
'''
# 만약 보석 A가 나오고 보석 B가 나온다고 하면([AAAAAAAAAAAAAAAAB]) A의 마지막 위치와 B의 최초 위치가 가장 짧은 구간이 될 것이다.
# 만약 보석 A가 나오고 보석 B 그리고고 마지막에C 가 순서대로 나온다고 하면([AABBAAABBABABAAABBC]) A의 마지막 위치나 B의 마지막 위치 그리고 C의 최초 위치 사이가 가장 짧은 구간이 될 것이다.
# 이때 구간에는 모든 보석이 들어가야 하므로 A와 B의 마지막 위치중 앞선것이 시작 위치가 되어야 한다.
# 여태까지는 마지막 보석이 마지막에 등장 했지만 언제 마지막 보석이 나올지 모른다. 또한 마지막 보석이 나온다고해서 그때까지 찾은 구간이 최소 길이라는 보장은 없다. 따라서 진열대는 전부 탐색해야한다.
# 하지만 논리는 위와 같다.
 
# 새로운 보석이 나타나면 구간을 갱신해야함
# 구간은 보석들의 마지막 위치 중 제일 앞 위치서 부터 다시 사작하면 됨
# 1. 구간의 맨앞 보석의 종류를 저장해둠
# 2. 보석의 마지막 위치를 저장할 딕셔너리를 만듬(이렇게 하면 딕셔너리 Value의 최소값과 최대값이 여태까지 탐색한 보석들의 구간의 길이가 된다.)
# 3. 구간 시작점을 저장
# 4. 보석의 마지막 위치는 그 보석이 나올 때 마다 계속 갱신해서 딕셔너리에는 보석의 종류와 마지막 위치만 기억하게 함
# 5. 보석들의 마지막 위치중 가장 앞에 있는 보석을 보석 X라고 하자
# 6. 들어온 보석이 X의 종류와 일치하면 갱신하고
# 7. 그 구간의 길이를 여태 찾은 답과 비교하여 짧은 쪽을 답으로 선택한다.(초깃값은 리스트의 길이+1)
def solution(gems):
    answer = []
    gemDict = {}
    startGem = gems[0]
    minLength = len(gems)+1
    min = 1
    for i,gem in enumerate(gems):
        if not gem in gemDict:
            minLength = i+1 - min + 1
            gemDict[gem] = i+1
            answer = [min,i+1]
        else:
            gemDict[gem] = i+1
            if gem == startGem:
                test = i
                for key, value in gemDict.items():
                    if value < test:
                        test = value
                        startGem = key
                length = i+1 - test +1
                if length < minLength:
                    minLength = length
                    answer=[test,i+1]
                min = test    
    return answer
gems = ["AA", "AA", "AA", "AA", "AB", "AA", "AA", "AA", "AB", "AC", "AC", "AC", "AC", "AC", "AC", "AC", "AC", "AA", "AA", "AA", "AA"]
print(solution(gems))
1, 2
2, 3
3, 4
4, 5
4, 5, 6
4, 6, 7
4, 6, 7, 8
6, 7, 8, 9


'''
# ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# ["XYZ", "XYZ", "XYZ"]
# ["AA", "AB", "AC", "AA", "AC"], ["AA", "AA", "AA", "AA", "AB", "AA", "AA", "AA", "AB", "AC", "AC", "AC", "AC", "AC", "AC", "AC", "AC", "AA", "AA", "AA", "AA"]
# ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
DR
DR...E
DR...ES
# ["D", "R", "R", "S", "R", "R", "D", "R", "S", "E", "E", "E", "R", "R", "S", "R", "D", "E", "S", "R", "R", "R", "R", "R", "R", "D", "G", "R", "R", "R", "R"]
# ["A","B","A","C","A","B","C"]
'''