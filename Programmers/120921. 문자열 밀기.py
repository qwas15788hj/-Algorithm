def solution(A, B):
    answer = -1
    if A==B:
        answer = 0
        return answer
    else:
        for i in range(1, len(A)):
            A = A[-1]+A[:-1]
            if A==B:
                answer = i
                break
            
    return answer