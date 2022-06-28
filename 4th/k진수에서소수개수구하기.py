# 10진수를 k진수로 바꿔서 str 형태로 반환하는 함수, k->10은 필요없음 k진수 상태로 10진법으로 소수 판별
def DToK(n,k):
    knumber = ""
    while True:
        tmp=str(n%k)
        n = n//k 
        knumber = "".join([tmp,knumber])
        if n == 0:
            return knumber
# 그 수가 소수인지 알려주는 함수.(단 1을 제외하고 알려준다.)   
def isPrimeNumber(test_number):
    k = 2
    while k**2 <= test_number:
        if test_number%k == 0:
            return False
        k += 1

    return True

def solution(n, k):
    answer = 0
    knumber = DToK(n,k)
    testnum_list = []
    # 0으로 나눠지는 숫자의 시작점을 나타낼 변수
    start = 0
    # K진수의 모든 자릿값에 대하여
    for i,number in enumerate(knumber):
        test_number = ""
        # 자릿값이 0이 나오면
        if number == "0":
            # 1. 전 자릿값이 0 였다면 0이 나오지 않을 때까지 넘어가고 시작 위치를 오른쪽으로 한칸 이동한다.
            if knumber[i-1] == "0":
                start = i+1
                pass
            # 2. 만약 전까지 이어지는 숫자의 나열이 있었다면,
            else:
                # 만약 그 숫자의 나열이 1이라면, 위에서 만든 소수판별 함수가 1을 판별해주지 못하므로 그냥 제외한다. 
                # 그리고 시작위치를 한칸 이동한다.   
                if knumber[start:i] != "1":
                    testnum_list.append(knumber[start:i])
                    start = i+1
                else:
                    start = i+1
        # 숫자 끝에서 0 이 아닌 수가 나온다면
        if i == len(knumber)-1:
            #위와 마찬가지 이유로, 1이 아니고, 숫자의 나열이 존재하면, 
            if knumber[start:] != "1" and knumber[start:]:
                testnum_list.append(knumber[start:])
                
    # 소수갯수를 반환한다.        
    for test_number in testnum_list:                 
        test_number = int(test_number)               
        if isPrimeNumber(test_number):
            answer += 1
                          
    return answer

n = 437674
k = 3

print(solution(n,k))