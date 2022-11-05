def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        prev = ""
        now = ""
        for b in bab:
            now += b
            if now!=prev and (now in arr):
                prev = now
                now = ""
        if len(now)==0:
            answer += 1
    
    return answer