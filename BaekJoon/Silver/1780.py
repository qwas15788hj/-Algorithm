n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

nav_cnt = 0 #-1개수
zero_cnt = 0 #0개수
one_cnt = 0 #1개수

def binary(paper):
    global nav_cnt, zero_cnt, one_cnt
    temp = paper[0][0] #기준점
    x = len(paper) #총 길이
    flag = True
    for i in range(x): #돌면서
        for j in range(x):
            if paper[i][j] != temp: #기준점이랑 값이 다르면
                flag = False #체크
                break
        if not flag:
            break

    if flag: #다 같다면
        if temp == -1:
            nav_cnt += 1
        elif temp == 0:
            zero_cnt += 1
        else:
            one_cnt += 1
    else: #틀리다면
        size = x//3 #3으로 나눈 길이
        for i in range(0, x, size): #세로 시작지점
            for j in range(0, x, size): #가로 시작지점
                sub_paper = [] #새로운 배열1
                for z in range(i, i+size): #세로 시작지점부터 나눈 개수까지
                    sub_paper2 = [] #새로운 배열1에 넣을 새로운 배열2
                    for k in range(j, j+size): #가로 시작지점부터 나눈 개수까지
                        sub_paper2.append(paper[z][k]) #새로운 배열2에 넣기
                    sub_paper.append(sub_paper2) #배열1에 배열2 넣기
                binary(sub_paper) #배열1 재귀

binary(arr)
print(nav_cnt)
print(zero_cnt)
print(one_cnt)