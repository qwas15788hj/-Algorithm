n, m = map(int, input().split()) #입력
k = int(input()) #구멍 개수 입력
arr = [[0]*(m+2) for _ in range(n+2)] #가로+2, 세로+2 배열 생성
for _ in range(k):
    x, y = map(int, input().split())
    arr[x][y] = -1 #구멍 표시

arr[1][1] = 1 #시작점 1
for i in range(1, m+1): #실제 벌집의 가로크기 만큼만 돌기
    for j in range(1, n+1): #실제 벌집의 세로크기 만큼만 돌기
        if i==1 and j==1: #처음 무시
            continue
        if arr[j][i] == -1: #구멍 0으로 변환 후 무시
            arr[j][i] = 0
            continue
        if i%2!=0: #홀수 인덱스 열 인덱스로 올 수 있는 방향 (위, 왼쪽 위, 왼쪽)
            arr[j][i] = arr[j-1][i] + arr[j-1][i-1] + arr[j][i-1]
        else: #짝수 인덱스 열 인덱스로 올 수 있는 방향 (위, 왼쪽, 왼쪽 아래)
            arr[j][i] = arr[j-1][i] + arr[j][i-1] + arr[j+1][i-1]

print((arr[n][m])%(pow(10, 9)+7))