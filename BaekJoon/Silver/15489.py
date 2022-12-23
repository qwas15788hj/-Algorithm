r, c, w = map(int, input().split()) # r, c, w 입력
arr = [[0]*(r+w-1) for _ in range(r+w-1)] # 최대 r+w-1크기의 DP 2차원 배열 생성
arr[0][0] = 1 # 첫자리 1

for i in range(1, len(arr)): # 2번째 줄~끝 줄까지
    for j in range(len(arr)): # 첫 열~ 끝 까지
        if j==0: # 왼쪽은 1
            arr[i][j] = 1
        elif i==j: # 헹==열 이면 1
            arr[i][j] = 1
        else: # 아니면 왼쪽위+위
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

answer = 0 # 정답
for i in range(w): # 몇 줄까지인지 반복
    for j in range(i+1): # 몇 열까지인지 반복
        answer += arr[r-1+i][c-1+j] # 시작지점인 arr[r-1][c-1] 에서 행은 i를 더해주고, 열은 j를 더해주기

print(answer)