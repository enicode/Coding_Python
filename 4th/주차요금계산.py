def fee( time, base_time, base_fee, unit_time, unit_fee):
    fee = 0
    if time <= base_time:
        fee = base_fee
    else:
        fee = base_fee + unit_fee * ((time-base_time)//unit_time if (time-base_time)%unit_time == 0 else (time-base_time)//unit_time + 1)
    return fee

def solution(fees, records):
    answer = []
    r = [[int(record[0:2])*60 + int(record[3:5]), record[6:10], record[11:]] for record in records]
    # 차량번호 순으로 정렬하고, 시간순으로 정렬, 들어가기도 전에 나올수는 없으므로 무조건 IN OUT 순으로 정렬 된다.
    # 또한 차량번호 순으로 정렬했으므로 순서대로 처리하여 answer에 더해주면 자동으로 차량번호순 정렬이 된다.
    r.sort(key = lambda x :(x[1],x[0]))
    
    base_time, base_fee, unit_time, unit_fee = fees
    
    end = 23*60+59
    #시간
    t = 0
    #요금
    f = 0
    for i in range(len(r)):
        # 만약 단 하나의 출입 기록만 있다면 IN 이고 이때 23:59 출차로 취급한다.
        if len(r) == 1:
            t = end - r[0][0]
            f = fee(t, base_time, base_fee, unit_time, unit_fee)
            answer.append(f)
            break
        # 처음에는 넘어가야한다. 볼 앞 값이 없으므로
        if i == 0:
            continue
        # 만약 앞의 값이 자기와 같고 자기가 OUT 이라면 주차시간에 (출차시간-입차시간)을 더해준다.
        if r[i][1] == r[i-1][1]:
            if r[i][2] == "OUT":
                t += r[i][0] - r[i-1][0]
        # 만약 다르다면
        elif r[i][1] != r[i-1][1]:
            # 다른데 앞에서 IN으로 끝났으면 그 차량의 마지막 출차기록이 없는 것이므로 23:59을 출차시간으로 하여 주차시간에 합산
            if r[i-1][2] == "IN":
                t += end - r[i-1][0]
            # 주차 요금을 계산하여 정답에 추가한다.
            if t <= base_time:
                f = fee(t, base_time, base_fee, unit_time, unit_fee)
                answer.append(f)
                # 시간과 요금 초기화
                f = 0
                t = 0
            else:
                f = fee(t, base_time, base_fee, unit_time, unit_fee)
                answer.append(f)
                f = 0
                t = 0
        # 마지막에 도달 하였는데
        if i == len(r)-1:
            # 입차로 끝났다면
            if r[i][2] == "IN":
                # 출차시간을 23:59으로 하여 주차시간에 더해준다.
                t += end - r[i][0]
            if t <= base_time:
                f = fee(t, base_time, base_fee, unit_time, unit_fee)
                answer.append(f)
            # 입차로 끝나지 않았다면 OUT으로 끝난것이고 그것은 이미 앞에서 계산하였다. 33줄
            else:               
                f = fee(t, base_time, base_fee, unit_time, unit_fee)
                answer.append(f)
        i += 1
               
    return answer



fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", 
           "06:00 0000 IN", 
           "06:34 0000 OUT", 
           "07:59 5961 OUT", 
           "07:59 0148 IN", 
           "18:59 0000 IN", 
           "19:09 0148 OUT", 
           "22:59 5961 IN", 
           "23:00 5961 OUT"]

print(solution(fees,records))

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

print(solution(fees,records))

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN",
           "16:00 0202 IN",
           "18:00 3961 OUT",
           "18:00 0202 OUT",
           "23:58 3961 IN"]
print(solution(fees, records))