# 로그가 30만개이므로 일일히 다 찾다가는 시간초과
from queue import PriorityQueue

def solution(play_time, adv_time, logs):
    answer = ''
    p = list(map(int , play_time.strip('\"').split(':')))
    # 영상 시간
    pt = 3600*p[0] + 60*p[1] + p[2]
    a = list(map(int , adv_time.strip('\"').split(':')))
    # 광고 시간
    at = 3600*a[0] + 60*a[1] + a[2]
    # 보는 사람숫자의 변화가 있는 시각에 [시각,변화]를 저장할 우선순위큐
    multi_time_list = PriorityQueue()

    for log in logs:
        hms_startl = list(map(int,log.strip('\"').split('-')[0].split(':')))
        hms_endl = list(map(int,log.strip('\"').split('-')[1].split(':')))
        # 시청 시작 시각    
        startl = 3600*hms_startl[0] + 60*hms_startl[1] + hms_startl[2]
        # 시청 종료 시각
        endl = 3600*hms_endl[0] + 60*hms_endl[1] + hms_endl[2]
        multi_time_list.put([startl,1])
        multi_time_list.put([endl,-1])
    # [시각, 보는사람]을 저장할 리스트
    multiflier= []
    tmp = 0
    # 우선순위 큐에서 꺼내서 담는다.
    for _ in range(len(logs)*2) :
        [time, multi] = multi_time_list.get()
        #시간순으로 꺼내므로 변화를 다 더하면 그 시각 보는 사람의 숫자이다.
        tmp += multi
        multiflier.append([time,tmp])

    #누적 재생시간을 저장할 리스트
    t_play_list = [0 for _ in range(pt+1)]
    # 모든 변화 있는 시각에 대해서
    for i in range(len(multiflier)-1):
        for time in range(multiflier[i][0]+1,multiflier[i+1][0]+1):
            # 현재시각 누적 재생시간 = 이전 시각 누적 재생시간 + 현재시청자수 이다.
            t_play_list[time] += t_play_list[time-1] + multiflier[i][1]
            
    maximum = 0
    hms = 0
     
    for time in range(pt-at+1):
        # 광고시간동안 누적 재생시간은 광고끝날때 누적재생시간 - 광고시작할 때 누적재생시간이다.
        t_play_time = t_play_list[time+at] - t_play_list[time]
        if maximum < t_play_time:
            maximum = t_play_time
            hms = time
            
    # 초를 글자로 변환
    h,m,s=0,0,0
    hs=''
    ms=''
    ss=''        

    h = hms//3600
    if h < 10:
        hs = f'0{h}'
    else:
        hs= f'{h}'
    hms -= h*3600

    m = hms//60
    if m < 10:
        ms = f'0{m}'
    else:
        ms = f'{m}'
    hms -= m*60

    s = hms
    if s< 10:
        ss = f'0{s}'
    else:
        ss = f'{s}'

    answer = f'{hs}:{ms}:{ss}'
    return answer

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))

play_time = "99:59:59"
adv_time = 	"25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))

play_time = "50:00:00"
adv_time = "50:00:00"
logs = 	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time, adv_time, logs))
