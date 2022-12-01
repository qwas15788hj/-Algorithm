from itertools import combinations

def solution(number):
    answer = 0
    
    number = list(combinations(number, 3))
    for num in number:
        if(sum(num)==0):
            answer+=1
    
    return answer