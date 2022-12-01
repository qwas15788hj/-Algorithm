dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def south(nx, ny, dir):
    for i in range(3, 0, -1):
        dice[i][1], dice[i-1][1] = dice[i-1][1], dice[i][1]

    if(arr[nx][ny]==0):
        arr[nx][ny] = dice[3][1]
    else:
        dice[3][1] = arr[nx][ny]
        arr[nx][ny] = 0

def east(nx, ny, dir):
    for i in range(2, 0, -1):
        dice[1][i], dice[1][i-1] = dice[1][i-1], dice[1][i]
    dice[1][0], dice[3][1] = dice[3][1], dice[1][0]

    if(arr[nx][ny]==0):
        arr[nx][ny] = dice[3][1]
    else:
        dice[3][1] = arr[nx][ny]
        arr[nx][ny] = 0

def west(nx, ny, dir):
    for i in range(2):
        dice[1][i], dice[1][i+1] = dice[1][i+1], dice[1][i]
    dice[1][2], dice[3][1] = dice[3][1], dice[1][2]

    if (arr[nx][ny] == 0):
        arr[nx][ny] = dice[3][1]
    else:
        dice[3][1] = arr[nx][ny]
        arr[nx][ny] = 0

def north(nx, ny, dir):
    for i in range(3):
        dice[i][1], dice[i+1][1] = dice[i+1][1], dice[i][1]

    if (arr[nx][ny] == 0):
        arr[nx][ny] = dice[3][1]
    else:
        dice[3][1] = arr[nx][ny]
        arr[nx][ny] = 0

n, m, x, y, k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

command = list(map(int, input().split()))
dice = [[0]*3 for _ in range(4)]

answer = []
for i in range(len(command)):
    nx, ny = x+dx[command[i]], y+dy[command[i]]
    if(nx<0 or nx>=n or ny<0 or ny>=m):
        continue
    if(command[i]==1):
        east(nx, ny, command[i])
    elif(command[i]==2):
        west(nx, ny, command[i])
    elif(command[i]==3):
        north(nx, ny, command[i])
    elif(command[i]==4):
        south(nx, ny, command[i])
    x, y = nx, ny
    answer.append(dice[1][1])

for i in answer:
    print(i)