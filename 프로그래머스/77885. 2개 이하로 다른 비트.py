def solution(numbers):
    answer = []
    
    for number in numbers:
        if number%2==0: #짝수는 +1
            answer.append(number+1)
        else: #홀수는
            n = 0
            num = "0"+bin(number)[2:]
            size = len(bin(number))
            for i in range(1, size):
                if(num[-i]=="0"): #0만날때까지
                    n = i
                    break
                    
            answer.append(number+pow(2, n-2)) #0만난 인덱스 -2만큼 2제곱 더하기
    
    return answer