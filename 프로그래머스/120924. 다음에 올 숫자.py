def solution(common):
    answer = 0
    
    arr = []
    for i in range(len(common)-1):
        arr.append(common[i+1]-common[i])
    
    if len(set(arr))==1:
        answer = common[-1]+arr[0]
    else:
        multi = arr[1]//arr[0]
        answer = common[-1]*multi
        
    return answer