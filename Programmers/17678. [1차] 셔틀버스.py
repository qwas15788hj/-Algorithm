def solution(n, t, m, timetable):
    answer = ''
    
    arr = []
    for time in timetable:
        ti = time.split(":")
        arr.append(int(ti[0])*60+int(ti[1]))
    arr.sort()
    
    last_time = []
    for i in range(n): #횟수만큼
        now = 540+(i*t) #버스도착시간
        # print("now>> {}" .format(now))
        if i==n-1: #막차
            for j in range(len(arr)): #남아있는 사람중
                if(arr[j] <= now): #탈수있는 사람이면
                    last_time.append(arr[j]) #막차에 저장
        else: #막차 아님
            cnt = 0 #뺀 사람 수
            for j in range(len(arr)):
                if(arr[j-cnt] <= now): #탈수 있는 사람이면
                    arr.pop(j-cnt) #빼기
                    cnt += 1
                if cnt == m: #다 타면 끝
                    break
    
    if len(last_time) < m: #막차에 탈 수 있다면 시간 출력
        h = str(now//60)
        m = str(now%60)
    else: #막차에 못 탈 것 같으면
        last_time.sort()
        last_time_pos = last_time[:m] #막차에 탈 수 있는 사람 중 빠른 m명 중
        con = max(last_time_pos)-1 #제일 마지막 사람보다 먼저 타기
        h = str(con//60)
        m = str(con%60)
    
    if len(h) < 2:
        h = "0"+h
    if len(m) < 2:
        m = "0"+m
    answer = h+":"+m
        
    return answer