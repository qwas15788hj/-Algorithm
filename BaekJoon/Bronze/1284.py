while True:
    n = int(input())
    if n == 0:
        break
    answer = 0
    for i in range(len(str(n))):
        if str(n)[i] == '1':
            answer += 2
        elif str(n)[i] == '0':
            answer += 4
        else:
            answer += 3
    answer += len(str(n)) + 1
    print(answer)