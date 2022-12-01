from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

town = []
def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    arr[x][y] = 0
    count = 1
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx = nx+dx[i]
            my = ny+dy[i]
            if 0<=mx<n and 0<=my<n:
                if arr[mx][my] == 1:
                    arr[mx][my] = 0
                    queue.append([mx, my])
                    count += 1
    town.append(count)

total = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i, j)
            total += 1

print(total)
town.sort()
for i in town:
    print(i)