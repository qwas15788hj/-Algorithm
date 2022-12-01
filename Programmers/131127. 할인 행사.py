def solution(want, number, discount):
    answer = 0
    arr = [0]*len(want)
    
    for i in range(len(discount)-9):
        arr = [0]*len(want)
        for j in range(10):
            if(discount[i+j] in want):
                arr[want.index(discount[i+j])] += 1
        
        flag = True
        for j in range(len(number)):
            if number[j]!=arr[j]:
                flag = False
                break
        
        if(flag==True):
            answer += 1
        
    return answer