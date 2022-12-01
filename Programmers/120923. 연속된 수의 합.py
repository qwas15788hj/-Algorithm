def solution(num, total):
    answer = []
    
    if num==1:
        answer.append(total)
    else:
        for i in range(num):
            answer.append(i)

        while True:
            if sum(answer)==total:
                break
            if sum(answer) > total:
                answer.pop()
                answer.insert(0, answer[0]-1)
            else:
                answer.pop(0)
                answer.append(answer[-1]+1)

    return answer