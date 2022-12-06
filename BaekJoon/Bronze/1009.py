t = int(input()) #테스트케이스
for _ in range(t): #반복
    a, b = map(int, input().split()) #입력
    num = 1 #처음 값: 1
    arr = [] #컴퓨터(나머지) 넣을 배열
    for i in range(b): #b만큼 반복하면서
        num = (num*a)%10 #현재 수*a 나머지 10
        if num==0: # num이 10의 배수면
            num = 10 #10번째 컴퓨터
        if num in arr: #num(나머지)가 배열에 존재한다면 멈추기
            break
        arr.append(num) #없다면 넣기
    print(arr[b%len(arr)-1]) #총b번 % 배열크기 -1 인덱스 출력