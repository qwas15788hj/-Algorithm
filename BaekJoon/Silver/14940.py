from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dist = [[0]*m for _ in range(n)]

queue = deque()
flag = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            queue.append([i, j])
            flag = True
            break
    if flag:
        break

count = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    size = len(queue)
    for _ in range(size):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and dist[nx][ny] == 0:
                queue.append([nx, ny])
                dist[nx][ny] = count
    count += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and dist[i][j] == 0:
            dist[i][j] = -1

for i in range(n):
    print(*dist[i])