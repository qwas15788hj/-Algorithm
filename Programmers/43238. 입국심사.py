def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n #가장 오래 걸리는 시간
    
    while left <= right:
        mid = (left+right)//2
        person = 0
        
        for time in times: #해당 시간동안 몇명의 사람이 심사를 받는지
            person += mid//time
        
        if person >= n: #너무 많은 사람들이 심사를 받음, 시간 줄이기, 답은 저장
            answer = mid
            right = mid-1
        else: #너무 적은 사람들이 심사를 받음, 시간 늘리기
            left = mid+1
    
    return answer