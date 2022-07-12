def solution(nums):
    answer = 0   
    dic = {}
    
    for p in nums:
        try:
            dic[p] += 1
        except KeyError:
            dic[p] = 1
            
    answer = int(min(len(nums)/2, len(dic)))
    return answer

nums = [3,3,3,2,2,4]
print(solution(nums))