from collections import deque

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*m for _ in range(n)]
count = 0
answer = 0

def bfs(x, y):
    global answer
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = True
    area = 1
    while queue:
        size = len(queue)
        for i in range(size):
            nx, ny = queue.popleft()
            for j in range(4):
                mx = nx+dx[j]
                my = ny+dy[j]
                if 0<=mx<n and 0<=my<m and not visited[mx][my] and arr[mx][my] == 1:
                    visited[mx][my] = True
                    area += 1
                    queue.append([mx, my])
    answer = max(answer, area)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
print(answer)