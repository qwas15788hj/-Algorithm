from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    global flag
    queue = deque()
    queue.append([x, y])
    arr[x][y] = 2
    while queue:
        nx, ny = queue.popleft()
        if nx == n-1:
            flag = True
            break
        for i in range(4):
            mx = nx + dx[i]
            my = ny + dy[i]
            if 0<=mx<n and 0<=my<m and arr[mx][my] == 0:
                arr[mx][my] = 2
                queue.append([mx, my])

flag = False
for i in range(m):
    if flag:
        break
    if arr[0][i] == 0:
        bfs(0, i)

if flag:
    print("YES")
else:
    print("NO")