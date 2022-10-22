def solution(genres, plays):
    answer = []
    
    gen_dict = dict() # 장르별 [인덱스, 플레이 횟수]
    play_dict = dict() # 장르별 총 플레이 수
    for i in range(len(genres)):
        if(genres[i] in gen_dict): #이미 있는 장르면
            gen_dict[genres[i]].append([i, plays[i]]) #해당 장르에 인덱스, 플레이 수 추가
            play_dict[genres[i]] += plays[i] #총 플레이 수 더하기
        else: #새로운 장르면
            gen_dict[genres[i]] = [[i, plays[i]]] #새로운 장르, 인덱스, 플레이 수 추가
            play_dict[genres[i]] = plays[i] #새로운 장르, 플레이 수 추가
    
    for gen in gen_dict:
        gen_dict[gen].sort(key=lambda x:(-x[1], x[0])) #장르별 플레이 수(오름차순), 인덱스(내림차순)
    
    while len(play_dict):
        for k, v in play_dict.items(): #플레이 딕셔너리 key, value
            if(v==max(play_dict.values())): #플레이 수가 가장 크면
                now_play = k #해당 장르 선택
                break
        for i in range(2):
            if(len(gen_dict[now_play])==0): #장르 딕셔너리에서 현재 장르 뽑을게 없음
                break
            answer.append(gen_dict[now_play][0][0]) #현재 장르의 인덱스 값
            del gen_dict[now_play][0] #장르 딕셔너리에서 현재 장르의 첫 번째 확인 한 것 없애기
        del play_dict[now_play] #플레이 딕셔너리에서 현재 확인한 장르 없애기
        
    return answer