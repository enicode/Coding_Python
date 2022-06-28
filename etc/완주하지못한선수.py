def solution(participant, completion):
    answer = ''
    pdict = {}
    for p in participant:        
        try:
            pdict[p] += 1
        except KeyError:
            pdict[p] = 1
    for c in completion:
        if pdict[c] == 1:
            del pdict[c]
        else:
            pdict[c] -=1 
    answer = str(list(pdict.keys())[0])
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))