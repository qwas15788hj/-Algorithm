from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = True
    target = arr[x][y]
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx = nx+dx[i]
            my = ny+dy[i]
            if 0<=mx<n and 0<=my<n:
                if arr[mx][my]==target and not visited[mx][my]:
                    visited[mx][my] = True
                    queue.append([mx, my])

visited = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
print(count, end=" ")

for i in range(n):
    for j in range(n):
        if arr[i][j]=="G":
            arr[i][j] = "R"

visited = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
print(count)