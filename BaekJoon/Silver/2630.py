n = int(input()) # n줄 입력
paper = [] # 첫 색종이
for _ in range(n): # 색종이 입력
    paper.append(list(map(int, input().split())))

white = 0 # 흰 종이
blue = 0 # 파란색 종이

def binary(arr): # 4등분하는 함수
    global white, blue
    size = len(arr) # 현재 확인하는 색종이의 크기
    half = size//2 # 크기 절반
    temp = arr[0][0] # 기준점
    flag = True
    for i in range(size): # 색종이를 돌면서
        for j in range(size):
            if arr[i][j] != temp: # 기준점과 다르면
                flag = False # 멈추기
                break
        if not flag:
            break

    if flag: # 기준점과 다 같다면
        if temp == 0: # 기준점이 0이면 흰 종이
            white += 1
        if temp == 1: # 기준점이 1이면 파란 종이
            blue += 1
    else: # 기준점과 다른게 있다면
        subarr = [] # 새로운 배열
        for i in range(half): # 왼쪽위 색종이
            subarr.append(arr[i][:half]) # 0~i행의 절반까지 열
        binary(subarr) # 함수돌기

        subarr = []
        for i in range(half): # 오른쪽위 색종이
            subarr.append(arr[i][half:size]) # 0~i행의 절반부터 끝까지
        binary(subarr)

        subarr = []
        for i in range(half, size): # 왼쪽아래 색종이
            subarr.append(arr[i][:half]) # 절반~끝까지 행의 절반까지 열
        binary(subarr)

        subarr = []
        for i in range(half, size): # 오른쪽아래 색종이
            subarr.append(arr[i][half:size]) # 절반~끝까지 행의 절반~끝까지
        binary(subarr)

binary(paper)
print(white)
print(blue)