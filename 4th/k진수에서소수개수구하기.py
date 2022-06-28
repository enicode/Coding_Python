def DToK(n,k):
    knumber = ""
    while True:
        tmp=str(n%k)
        n = n//k 
        knumber = "".join([tmp,knumber])
        if n == 0:
            return knumber
    
def KToD(knumber, k):
    dnumber = 0
    for i,number in enumerate(reversed(knumber)):
        dnumber += int(number)*(k**i)
    return dnumber
    
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
    start = 0
    testnum_list = []
    for i,number in enumerate(knumber):
        test_number = ""
        k = 0
        if number == "0":
            if knumber[i-1] == "0":
                start = i+1
                pass
            else:
                if knumber[start:i] != "1":
                    testnum_list.append(knumber[start:i])
                    start = i+1
                else:
                    start = i+1
        if i == len(knumber)-1:
            if knumber[start:] != "1" and knumber[start:]:
                testnum_list.append(knumber[start:])
                
    print(testnum_list)               
    for test_number in testnum_list:                 
        test_number = int(test_number)               
        if isPrimeNumber(test_number):
            answer += 1
                          
    return answer

n = 437674
k = 3

print(solution(n,k))