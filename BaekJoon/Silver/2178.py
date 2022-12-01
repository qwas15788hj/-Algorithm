from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    arr[x][y] = 1
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx = nx+dx[i]
            my = ny+dy[i]
            if 0<=mx<n and 0<=my<m:
                if arr[mx][my] == 0:
                    continue
                elif arr[mx][my] == 1:
                    arr[mx][my] = arr[nx][ny] + 1
                    queue.append([mx, my])

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

bfs(0, 0)
print(arr[n-1][m-1])