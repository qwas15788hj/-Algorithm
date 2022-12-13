n = int(input()) # n입력
mvp = list(map(int, input().split())) # mvp 기준액 입력
grade = input() # 등급입력

money = [0]*(n+1) # 달마다 과금액 저장할 배열 처음은 0원
for i in range(n): # n번의 달 돌면서 가능한 최대 과금액 구하기
    if grade[i] == "D": # 다이아 등급이라면
        money[i+1] = mvp[3] # 현재 달에 과금액은 다이아등급 값
    else:
        if grade[i] == "B": # 브론즈 등급이라면
            cash = mvp[0]-1 # 실버 등급 금액-1
        elif grade[i] == "S": # 실버 등급이라면
            cash = mvp[1]-1 # 골드 등급 금액-1
        elif grade[i] == "G": # 골드 등급이라면
            cash = mvp[2]-1 # 플레티넘 등급 금액-1
        elif grade[i] == "P": # 플레티넘 등급이라면
            cash = mvp[3]-1 # 다이아 등급 금액-1
        money[i + 1] = cash - money[i] # 현재 달 과금액 = 구한 과금액 - 지난달 금액

print(sum(money))