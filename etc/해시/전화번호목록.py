from collections import defaultdict
def solution(phone_book):
    answer = True
    pn_dic = defaultdict(int)
    # 전화번호 딕셔너리를 만든다.
    for p_number in phone_book:
        pn_dic[p_number] = True
    # 최소길이 전화번호보다 길이가 긴 전화번호에 대해서만
    for p_number in phone_book:
        for i in range(len(p_number)):
            if pn_dic[p_number[:i]]:
                return False
    return answer

phone_book = ["11","12","111"]

print(solution(phone_book))