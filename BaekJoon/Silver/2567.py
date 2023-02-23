n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                print(nx, ny)
                if arr[nx][ny] == 1:
                    cnt += 1
            if cnt == 3:
                answer += 1
            elif cnt == 2:
                answer += 2

print(answer)