import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0]*n for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        arr[i][j] = num
        num += 1

#오른쪽으로 한칸 움직이는 함수
def row(x):
    #오른쪽 끝부터 시작해 앞쪽과 스왑
    for i in range(n-1, 0, -1):
        arr[x][i-1], arr[x][i] = arr[x][i], arr[x][i-1]

#아래로 한칸 움직이는 함수
def column(x):
    #아래 끝부터 시작해 위쪽과 스왑
    for i in range(n-1, 0, -1):
        arr[i-1][x], arr[i][x] = arr[i][x], arr[i-1][x]

for _ in range(k):
    x, r, c = map(int, input().split()) #이동하려는 수, 이동해야하는 위치 r(행), c(열) => arr[r][c]
    r -= 1 #인덱스이므로 -1
    c -= 1 #인덱스이므로 -1
    now_r = 0 #이동하려는 수 현재 행 위치, 세로
    now_c = 0 #이동하려는 수 현재 열 위치, 가로
    flag = False
    for i in range(n): #해당 숫자 찾기
        if flag:
            break
        for j in range(n):
            if arr[i][j] == x:
                now_r = i
                now_c = j
                flag = True
                break
    #몇 번 움직여야하는지, 가로
    if c >= now_c: #목표 위치가 현재 위치보다 크거나 작으면
        count_c = c - now_c
    else: #목표 위치가 현재 위치보다 작으면
        count_c = n+c - now_c #돌아가야 하기에 +n
    #함수 호출
    for i in range(count_c):
        row(now_r)

    #갱신된 위치 다시 찾기
    flag = False
    for i in range(n):
        if flag:
            break
        for j in range(n):
            if arr[i][j] == x:
                now_r = i
                now_c = j
                flag = True
                break

    #몇 번 움직여야하는지, 세로
    if r >= now_r: #목표 위치가 현재 위치보다 크거나 작으면
        count_r = r - now_r
    else: #목표 위치가 현재 위치보다 작으면
        count_r = n+r - now_r #돌아가야 하기에 +n
    #함수 호출
    for i in range(count_r):
        column(now_c)

    print(count_r+count_c)