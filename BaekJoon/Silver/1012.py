from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    arr[x][y] = 0
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx = nx+dx[i]
            my = ny+dy[i]
            if 0<=mx<n and 0<=my<m and arr[mx][my]==1:
                queue.append([mx, my])
                arr[mx][my] = 0

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                bfs(i, j)
                count += 1
    print(count)