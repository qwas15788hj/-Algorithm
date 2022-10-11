from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sit(student):
    my = student[0]
    love = student[1:5]
    student_sit = []
    for i in range(n):
        for j in range(n):
            if(arr[i][j]==0):
                x = i
                y = j
                block_cnt = 0
                love_cnt = 0
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if(0<=nx<n and 0<=ny<n):
                        if(arr[nx][ny]==0):
                            block_cnt+=1
                        else:
                            if(arr[nx][ny] in love):
                                love_cnt += 1

                student_sit.append([x, y, block_cnt, love_cnt])

    student_sit.sort(key=lambda x:(-x[3], -x[2], x[0], x[1]))
    arr[student_sit[0][0]][student_sit[0][1]] = my


def bfs(x, y):
    my = arr[x][y]
    for i in range(len(student)):
        if(student[i][0]==my):
            love = student[i][1:5]
            break

    count = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(0<=nx<n and 0<=ny<n and arr[nx][ny] in love):
            count += 1

    global answer
    answer += int(10**(count-1))



n = int(input())
arr = [[0]*n for _ in range(n)]
student = []
for _ in range(n*n):
    student.append(list(map(int, input().split())))

for i in range(len(student)):
    sit(student[i])

answer = 0
for i in range(n):
    for j in range(n):
        bfs(i, j)

print(answer)